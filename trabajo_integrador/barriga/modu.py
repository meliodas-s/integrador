# Se importan modulo
import pandas as pd
import numpy as np
from . import helpers as hlp
import sympy as sp
from IPython.display import display
from .modelos.barra import Barra


class Rock():
    '''Calcula la matriz de rigidez global.
    Así como los vectores de desplazamientos y fuerzas nodales.

    Parameters
    ----------
    inc : array_like
        Matriz de incógnitas. Cada fila representa una variable con las
        columnas: (fuerza, desplazamiento).

    ino : array_like
        Matriz de índices de nodos. Cada fila representa un nodo y contiene las
        columnas: (número de nodo, índice de momento, índice de fuerza en x,
        índice de fuerza en y).
    '''

    def __init__(self, inc, iba, ino, pri=False):

        # Input fuerzas e incognitas (encognitas)
        ncc = ['fue', 'des']
        inc = pd.DataFrame(inc, columns=ncc)

        # Input barras
        bac = ['bar', 'noi', 'nof', 'are', 'mod', 'ine']
        iba = pd.DataFrame(iba, columns=bac)

        # Input nodos
        noc = ['nod', 'imn', 'ifx', 'ify', 'cox', 'coy']
        ino = pd.DataFrame(ino, columns=noc)

        # Input nodos cambiando indice
        ini = ino.set_index('nod')

        # Cantidad de nodos
        can = ini.shape[0]

        # Cantidad de libertades
        lib = can*3

        # Numeracion del 1 al n(numero de libertades)
        nli = np.arange(1, lib+1)

        # Crear data-frame de rigidez
        rig = pd.DataFrame(0, index=nli, columns=nli).astype(float)

        # Lista de barras
        lba: list[Barra] = []

        # Merge de datos
        for idx, fil in iba.iterrows():

            # Nodos que conectan a esa barra
            noi = fil['noi']
            nof = fil['nof']

            # Creo una nueva barra
            lba.append(
                Barra(
                    int(fil['bar']),
                    fil['noi'],
                    fil['nof'],
                    fil['are'],
                    fil['mod'],
                    fil['ine'],
                    ini.loc[int(fil['noi']), 'imn'],
                    ini.loc[int(fil['noi']), 'ifx'],
                    ini.loc[int(fil['noi']), 'ify'],
                    ini.loc[int(fil['nof']), 'imn'],
                    ini.loc[int(fil['nof']), 'ifx'],
                    ini.loc[int(fil['nof']), 'ify'],
                    ini.loc[noi, 'cox'],
                    ini.loc[nof, 'cox'],
                    yfi=ini.loc[nof, 'coy'],
                    yin=ini.loc[noi, 'coy']
                ))
            lba[idx].cal_lar()
            lba[idx].cal_lmx()
            lba[idx].cal_lmy()
            lba[idx].cal_tra()
            lba[idx].cal_ril()
            lba[idx].cal_rig()

            # Agrego los esfuerzos a esta barra
            hlp.mrb(lba[idx], rig)

        # Se crea matriz symbolica rigSimbolica
        rgs = sp.Matrix(rig.values)

        if pri:
            hlp.col("Matriz de rigidez")
            display(rgs.evalf(5))

        # Defino Matrizes de Desplaza e Incog.(fuerzas)
        mde = sp.Matrix()
        min = sp.Matrix()

        # Defino Incog. Simbolicas de Desplaza y Fuerzas
        isd = sp.Matrix()
        isf = sp.Matrix()

        # Incognitas totales
        igt = []

        # Se crean los datos de las incognitas
        for idx, fil in inc.iterrows():
            if not fil['des']:
                fue = sp.symbols(f'Q_{idx + 1}')
                mde = mde.col_join(sp.Matrix([0]))
                min = min.col_join(sp.Matrix([fue]))

                # Agrego la incognita fuerza
                isd = isd.col_join(sp.Matrix([0]))
                isf = isf.col_join(sp.Matrix([fue]))
                igt.append(fue)

            else:
                des = sp.symbols(f'D_{idx + 1}')
                mde = mde.col_join(sp.Matrix([des]))
                min = min.col_join(sp.Matrix([fil['fue']]))

                # Agrego la incognita despla
                isd = isd.col_join(sp.Matrix([des]))
                isf = isf.col_join(sp.Matrix([fil['fue']]))
                igt.append(des)

        # Matriz resultante de incognitas
        res = rgs * mde
        eqs = []

        # Imprimiendo
        if pri:
            hlp.col("Matriz de desplazamiento:")
            display(mde)

        # Cargo eqs con los items de res
        for idx in range(res.rows):
            eqs.append(sp.Eq(min[idx], res[idx]))

        sol = sp.solve(eqs, igt)
        isd = isd.subs(sol)
        isf = isf.subs(sol)

        if pri:
            hlp.col("Soluciones:")
            display(sp.Eq(
                sp.Matrix(list(sol.keys())),
                sp.Matrix(list(sol.values())))
            )

        # Defino la matriz de soluciones
        self.ret = dict()

        # Consigo los valores de las fuerzas en las barras
        for ib in lba:

            # Desplazamiento de los nodos en x e y
            den = [ib.nix, ib.niy, ib.nim, ib.nfx, ib.nfy, ib.nfm]

            # Vector de desplazamientos: [DNx, DNy, DFx, DFy]
            vde = np.array(
                [
                    isd[int(den[0])-1],
                    isd[int(den[1])-1],
                    isd[int(den[2])-1],
                    isd[int(den[3])-1],
                    isd[int(den[4])-1],
                    isd[int(den[5])-1],
                ]
            )

            # Cálculo del esfuerzo de la barra
            esf = (ib.ril@ib.tra)@vde

            if pri:
                hlp.col(f"Fuerza en barra {ib.bar}")
                display(pd.DataFrame(esf, index=den, columns=[f'{ib.bar}']))

            # Guardo los valores
            self.ret[f'{idx+1}'] = esf
            self.isd = isd
