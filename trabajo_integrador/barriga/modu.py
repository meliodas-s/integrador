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

# clases
from typing import Literal

# h(orizontal), v(vertical), n(ninguna)
TipoCarga = Literal["h", "v", "n"]


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
        incog: list,
        iba: list,
        ino: list,
        car: list,
        sop: list,
        conf: list,
        desig: dict,
        tipo: TipoCarga = 'n',
        cag: int = 0,
        pesos: list = None,
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

        # cantidad de barras
        self.can = None

        # designaciones de barras
        self.desig: dict = desig

        # lista de barras
        self.lba: list[Barra] = list()

        # situacion a analizar
        self.sit: TipoCarga = tipo

        # multiplo de gravedad
        self.cag = cag

        # peso adjunto a cada barra
        self.pes = pesos

        # Input fuerzas e incognitas (encognitas)
        ncc = ['fue', 'des']
        self.inc = pd.DataFrame(incog, columns=ncc)

        # dataframe barras
        bac = ['bar', 'noi', 'nof', 'are', 'mod', 'ine']
        self.iba = pd.DataFrame(iba, columns=bac)
        self.can = self.iba.shape[0]

        # Input nodos
        noc = ['nod', 'imn', 'ifx', 'ify', 'cox', 'coy']
        ino = pd.DataFrame(ino, columns=noc)
        self.ini = ino.set_index('nod')

        # cargo las barras
        self.car_bar()

        # cargo los desplazamientos
        self.car_des(car)

        # input de cargas
        self.cgs: list[Carga] = []
        for i in car:
            self.cgs.append(Carga(i[0], i[1], i[2]))

        # input de soportes
        self.lso = list()
        for i in sop:
            self.cre_sop(i)

        # Cantidad de libertades
        self.cal = self.inc.shape[0]

        # Numeracion del 1 al n(numero de libertades)
        nli = np.arange(1, self.cal+1)

        # Crear data-frame de rigidez
        self.rig = pd.DataFrame(0, index=nli, columns=nli).astype(float)

        # se suma todo en la matriz de rigidez
        for bar in self.lba:
            hlp.mrb(bar, self.rig)

        # se crea matriz symbolica rigSimbolica
        rgs = sp.Matrix(self.rig.values)

        # defino matrizes de Desplaza e Incog.(fuerzas)
        mde = sp.Matrix()
        min = sp.Matrix()

        # defino incog. simbolicas de Desplaza y Fuerzas
        isd = sp.Matrix()
        isf = sp.Matrix()

        # incognitas totales
        igt = []

        # se crean los datos de las incognitas
        for idx, fil in self.inc.iterrows():
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
        for bar in self.lba:

            # desplazamiento de los nodos en x e y
            den = [bar.nix, bar.niy, bar.nim, bar.nfx, bar.nfy, bar.nfm]

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
            esf = (bar.ril@bar.tra)@vde
            esf = pd.DataFrame(esf, index=den, columns=[f'{bar.bar}'])

            # guardo los valores
            bar.esf = esf

        # momentos en barras con cargas
        for cag in self.cgs:

            # indice de barra
            iba = cag.bar

            # barra en cuestion
            bar = self.lba[iba-1]

            match cag.tip:
                case 1:
                    bar.cav = cag
                case 2:
                    bar.cah = cag
                case 3:
                    bar.cat = cag

        for i in self.lba:
            # se calculan los momentos
            i.cal_mom()
            i.cal_cor()
            i.cal_nor()

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

    def car_bar(self):
        '''Funcion encargada de cargar barras'''
        # merge de datos
        for idx, fil in self.iba.iterrows():

            # nodos que conectan a esa barra
            noi = fil['noi']
            nof = fil['nof']

            # creo una nueva barra
            self.lba.append(
                Barra(
                    int(fil['bar']),
                    fil['noi'],
                    fil['nof'],
                    fil['are'],
                    fil['mod'],
                    fil['ine'],
                    self.ini.loc[int(fil['noi']), 'imn'],
                    self.ini.loc[int(fil['noi']), 'ifx'],
                    self.ini.loc[int(fil['noi']), 'ify'],
                    self.ini.loc[int(fil['nof']), 'imn'],
                    self.ini.loc[int(fil['nof']), 'ifx'],
                    self.ini.loc[int(fil['nof']), 'ify'],
                    self.ini.loc[noi, 'cox'],
                    self.ini.loc[nof, 'cox'],
                    desig=self.desig[int(fil['bar'])],
                    yfi=self.ini.loc[nof, 'coy'],
                    yin=self.ini.loc[noi, 'coy'],
                ))
            self.lba[idx].cal_lar()
            self.lba[idx].cal_lmx()
            self.lba[idx].cal_lmy()
            self.lba[idx].cal_tra()
            self.lba[idx].cal_ril()
            self.lba[idx].cal_rig()
            self.lba[idx].cal_ang()

    def car_des(self, cag: list):
        '''funcion encargada de cargar nodos
        dependiendo si es una situacion de carga verticales
        o cargas horizonales. Ejemplo: un choque o el peso
        mismo de la estructura

        - Por convencion el signo de la carga vertical
        ira positivo si es que la carga va de arriba a abajo
        '''
        grav = 9.8

        match self.sit:

            # gravedad Nm/s2
            case 'h':
                print(self.pes)
                pass

            case 'v':
                print(self.pes)
                for bar in self.lba:
                    bar.mas = self.pes[bar.bar]

                    # creo carga vertical [N/m2]
                    cargv = grav*self.cag*bar.mas/bar.lar

                    # componentes en x e y
                    cargvx = -cargv*np.sin(bar.ang)
                    cargvy = cargv*np.cos(bar.ang)

                    # fuerzas verticales en ambos nodods
                    qv = cargv*bar.lar/2

                    # momento en a (nodo incia)
                    moi = -cargvy*bar.lar**2/12

                    # momento en a (nodo final)
                    mof = cargvy*bar.lar**2/12

                    # se suman los datos a las incognitas
                    self.inc.at[bar.nim-1, 'fue'] += round(moi, 5)
                    self.inc.at[bar.nfm-1, 'fue'] += round(mof, 5)
                    self.inc.at[bar.niy-1, 'fue'] += -qv
                    self.inc.at[bar.nfy-1, 'fue'] += -qv

                    # se guardan las cargas
                    cag.append([bar.bar, 1, round(cargvy, 5)])
                    cag.append([bar.bar, 2, round(cargvx, 5)])

                    print(
                        f"""
                        bar{bar.bar}
                            masa:{bar.mas}
                            carg:{cargv}
                            rad:{bar.ang}
                            qx:{cargvx}
                            qy:{cargvy}
                            v:{qv}
                            mb: {mof}
                            ma: {moi}
                            lar{bar.lar}
                        """)

            case 'n':
                pass

    def grf_est(self):
        gre = GrfEst(self.lba, self.lso, self.conf)
        gre.graficar()
        gre.guardar(gre.fig, 'gre.png')
        gre.muestra()

    def grf_mom(self):
        grm = GrfMom(self.lba, self.lso, self.conf)
        grm.cargado()
        grm.graficar()
        grm.guardar(grm.fig, 'grm.png')
        grm.muestra()

    def grf_nor(self):
        grn = GrfNor(self.lba, self.lso, self.conf)
        grn.cargado()
        grn.graficar()
        grn.guardar(grn.fig, 'grn.png')
        grn.muestra()

    def grf_cor(self):
        grc = GrfCor(self.lba, self.lso, self.conf)
        grc.cargado()
        grc.graficar()
        grc.guardar(grc.fig, 'grc.png')
        grc.muestra()

    # def grf_des(self):
    #     pass
