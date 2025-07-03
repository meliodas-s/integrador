'''
Se desarrolla la version modular
del ejercicio para poder trabajarla en un jupyter.
'''

# Se importan modulo
import pandas as pd
import numpy as np
from . import helpers as hlp
import sympy as sp
from dataclasses import dataclass
from IPython.display import display


class Rock():
    '''
    Calcula la matriz de rigidez, desplazamientos y fuerzas.

    Parameters
    ----------
    inc: array_like
        Incognitas con las columnas (fuerza, desplazamiento)

    ino: array_like
        Indice de nodos con las columnas 
        (numero de nodo, indice de momento, indice de fuerx, indice de fuery)
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
            # Agrego una nueva barra
            # lba.append(Barra())

            noi = fil['noi']
            nof = fil['nof']
            bar = fil['bar']

            # Coordenadas x
            xin = ini.loc[noi, 'cox']
            xfi = ini.loc[nof, 'cox']

            # Coordenadas y
            yfi = ini.loc[nof, 'coy']
            yin = ini.loc[noi, 'coy']

            # Largo (funcion distancia)
            lar = np.sqrt((xfi-xin)**2+(yfi-yin)**2)

            # Guardando en array
            iba.loc[idx, 'lar'] = lar

            # Calculando lambdax y lambday
            iba.loc[idx, 'lmx'] = (xfi-xin)/lar
            iba.loc[idx, 'lmy'] = (yfi-yin)/lar

            # print(int(fil['nof']))
            # print(ino.loc[int(fil['nof'])])

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

            # Agrego los esfuerzos a esta barra
            hlp.mrb(iba.iloc[idx], ini, rig, lba[idx])

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


@dataclass
class Barra:
    """
    Clase que representa una barra estructural de un sistema en 2D o 3D.

    Atributos:
    ----------
    bar : int
        Identificador único de la barra.

    noi : int
        Nodo inicial de la barra (ID del nodo).

    nof : int
        Nodo final de la barra (ID del nodo).

    are : float
        Área de la sección transversal de la barra (en unidades consistentes).

    mod : float
        Módulo de elasticidad del material (E) o módulo de Young.

    ine : float
        Momento de inercia de la barra respecto a su eje transversal.

    tra : np.array
        Matriz de transformación que relaciona coordenadas locales y globales.

    rig : np.array
        Matriz de rigidez.

    nim : int
        Índice global asociado al momento en el nodo inicial.

    nix : int
        Índice global asociado a la fuerza en X en el nodo inicial.

    niy : int
        Índice global asociado a la fuerza en Y en el nodo inicial.

    nfm : int
        Índice global del momento en el nodo final.

    nfx : int
        Índice global de la fuerza en X en el nodo final.

    nfy : int
        Índice global de la fuerza en Y en el nodo final.
    """
    bar: int
    noi: int
    nof: int
    are: float
    mod: float
    ine: float
    nim: int
    nix: int
    niy: int
    nfm: int
    nfx: int
    nfy: int
    xin: float
    xfi: float
    yin: float
    yfi: float
    tra: np.array = None
    rig: np.array = None

    def cal_lmx(self):
        self.lmx = (self.xfi-self.xin)/self.lar

    def cal_lmy(self):
        self.lmy = (self.yfi-self.yin)/self.lar

    def cal_tra(self):
        # Matris de transformacion
        self.tra = (
            np.array(
                [
                    [self.lmx, self.lmy, 0, 0, 0, 0],
                    [-self.lmy, self.lmx, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, self.lmx, self.lmy, 0],
                    [0, 0, 0, -self.lmy, self.lmx, 0],
                    [0, 0, 0, 0, 0, 1]
                ]
            )
        )

    def cal_rig(self):
        pass

    def cal_lar(self):
        self.lar = np.sqrt((self.xfi-self.xin)**2+(self.yfi-self.yin)**2)

    # # Hay terminos repetirdos
    # te1 = are*mod/lar
    # te2 = 12*mod*ine/lar**3
    # te3 = 6*mod*ine/lar**2
    # te4 = 4*mod*ine/lar
    # te5 = 2*mod*ine/lar

    # # Matriz rigidez local de la barra (k`)
    # mrl = (
    #     np.array(
    #         [
    #             [te1, 0, 0, -te1, 0, 0],
    #             [0, te2, te3, 0, -te2, te3],
    #             [0, te3, te4, 0, -te3, te5],
    #             [-te1, 0, 0, te1, 0, 0],
    #             [0, -te2, -te3, 0, te2, -te3],
    #             [0, te3, te5, 0, -te3, te4]
    #         ]
    #     )
    # )
    
    # # Guardo la matriz de rigidex local
    # brc.ril = mrl

    # # Calculo la matriz de rigidez global (k) y guardo.
    # brc.rig = (tra.T@mrl)@tra