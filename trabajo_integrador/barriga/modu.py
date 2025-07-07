# Se importan modulo
import pandas as pd
import numpy as np
from . import helpers as hlp
import sympy as sp
from .modelos.barra import Barra
from .modelos.carga import Carga
from .vistas.estructura import GrfEst
from .vistas.esfuerzo import GrfMom, GrfNor, GrfCor
from .modelos.config import Conf

# soportes
from .modelos.soportes import ViculoSeg, ViculoPri, viculoTer


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

    def cre_sop(self, soi):
        '''Funcion encargada de crear soporte

        Parameters
        ----------
        soi : list
            soporte individual a crearse y guardarse.
        '''

        tip = soi[0]
        nod = soi[1]
        ang = soi[2]
        match tip:
            case 1:
                self.lso.append(ViculoPri(self.ini.loc[nod], ang))
            case 2:
                self.lso.append(ViculoSeg(self.ini.loc[nod], ang))
            case 3:
                self.lso.append(viculoTer(self.ini.loc[nod], ang))

    def __init__(
        self,
        inc: list,
        iba: list,
        ino: list,
        car: list,
        sop: list,
        conf: list,
        pri=False
    ):

        # input de config
        self.conf = Conf(*conf)

        # dataframe con nodos
        self.ini = None

        # lista con soportes
        self.lso = None

        # lista con incognitas de desplazamiento
        self.isd = None

        # lista con incognitas de esfuerzos
        self.isf = None

        # matriz de rigidez
        self.rig = None

        # matriz de desplazamiento
        self.mde = None

        # matriz de fuerza
        self.min = None

        # ecuaciond e igualdades, incognitas
        self.ecu = None

        # Input de cargas
        cgs: list[Carga] = []
        for i in car:
            cgs.append(Carga(i[0], i[1], i[2]))

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
        self.ini = ini

        # Input de soportes
        self.lso = list()
        for i in sop:
            self.cre_sop(i)

        # Cantidad de libertades
        can = inc.shape[0]

        # Numeracion del 1 al n(numero de libertades)
        nli = np.arange(1, can+1)

        # Crear data-frame de rigidez
        rig = pd.DataFrame(0, index=nli, columns=nli).astype(float)

        # lista de barras
        lba: list[Barra] = []

        # merge de datos
        for idx, fil in iba.iterrows():

            # nodos que conectan a esa barra
            noi = fil['noi']
            nof = fil['nof']

            # creo una nueva barra
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

            # agrego los esfuerzos a esta barra
            hlp.mrb(lba[idx], rig)

        # se crea matriz symbolica rigSimbolica
        self.rig = rig
        rgs = sp.Matrix(rig.values)

        # defino matrizes de Desplaza e Incog.(fuerzas)
        mde = sp.Matrix()
        min = sp.Matrix()

        # defino incog. simbolicas de Desplaza y Fuerzas
        isd = sp.Matrix()
        isf = sp.Matrix()

        # incognitas totales
        igt = []

        # se crean los datos de las incognitas
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

        # guardo datos
        self.mde = mde
        self.min = min

        # matriz resultante de incognitas
        res = rgs * mde
        eqs = []

        # cargo eqs con los items de res
        for idx in range(res.rows):
            eqs.append(sp.Eq(min[idx], res[idx]))

        sol = sp.solve(eqs, igt)
        isd = isd.subs(sol)
        isf = isf.subs(sol)

        # guardo las soluciones
        self.isd = isd
        self.isf = isf

        # guardo la ecuaciond de igualdades
        self.ecu = sp.Eq(
            sp.Matrix(list(sol.keys())),
            sp.Matrix(list(sol.values()))
        )

        # consigo los valores de las fuerzas en las barras
        for ib in lba:

            # desplazamiento de los nodos en x e y
            den = [ib.nix, ib.niy, ib.nim, ib.nfx, ib.nfy, ib.nfm]

            # vector de desplazamientos [DNx, DNy, DFx, DFy]
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

            # cálculo del esfuerzo de la barra
            esf = (ib.ril@ib.tra)@vde
            esf = pd.DataFrame(esf, index=den, columns=[f'{ib.bar}'])

            # guardo los valores
            ib.esf = esf

        # momentos en barras con cargas
        for cag in cgs:

            # indice de barra
            iba = cag.bar

            # barra en cuestion
            bar = lba[iba-1]

            match cag.tip:
                case 1:
                    bar.cav = cag
                case 2:
                    bar.cah = cag
                case 3:
                    bar.cat = cag

        for i in lba:
            # se calculan los momentos
            i.cal_mom()
            i.cal_cor()
            i.cal_nor()

        # se guardan las barras en el objeto Rock
        self.lba = lba

        if pri:
            self.imprimi()

    def imprimi(self):

        hlp.col("Matriz de rigidez")
        print(self.rig.to_string())

        hlp.col("Matriz de Fuerzas:")
        sp.pprint(self.min)

        hlp.col("Matriz de desplazamiento:")
        sp.pprint(self.mde)

        hlp.col("Soluciones:")
        sp.pprint(self.ecu)

        for i in self.lba:
            hlp.col(f"Barra: {i.bar}")
            hlp.col(f"Matriz sistema global:")
            print(i.rgi.to_string())
            
            hlp.col(f"Esfuerzos:")
            sp.pprint(i.esf)

    def grf_est(self):
        gre = GrfEst(self.lba, self.lso, self.conf)
        gre.graficar()
        gre.guardar(gre.fig, 'gre.pdf')
        gre.muestra()

    def grf_mom(self):
        grm = GrfMom(self.lba, self.lso, self.conf)
        grm.cargado()
        grm.graficar()
        grm.guardar(grm.fig, 'grm.pdf')
        grm.muestra()

    def grf_nor(self):
        grn = GrfNor(self.lba, self.lso, self.conf)
        grn.cargado()
        grn.graficar()
        grn.guardar(grn.fig, 'grn.pdf')
        grn.muestra()

    def grf_cor(self):
        grc = GrfCor(self.lba, self.lso, self.conf)
        grc.cargado()
        grc.graficar()
        grc.guardar(grc.fig, 'grc.pdf')
        grc.muestra()

    # def grf_des(self):
    #     pass
