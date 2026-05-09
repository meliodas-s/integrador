# Se importan modulo
import pandas as pd
import numpy as np
import sympy as sp
from . import helpers as hlp
from .modelos.barra import Barra
from .modelos.carga import Carga
from .vistas.estructura import GrfEst
from .vistas.esfuerzo import GrfMom, GrfNor, GrfCor
from .modelos.config import Conf
from .control.ctr_nod import CtrN
from .control.ctr_bar import CtrB
from .modelos.matri import SolvIt

# soportes
from .modelos.soportes import Vinculo, ViculoSeg, ViculoPri, viculoTer

# clases
from typing import Literal

# h(orizontal), v(vertical), n(ninguna)
TipoCarga = Literal["h", "v", "n"]


class Rock():
    '''Calcula la matriz de rigidez global.
    Así como los vectores de desplazamientos y fuerzas nodales.

    Parameters
    ----------
    conf: configuraciones
    lso: lista de soportes
    isf: incognitas de esfuerzos
    rig: matriz de rigidez de la estructura
    mde: matriz de desplazamiento de la estructura
    min: matriz de incofnitas de fuerzas
    ecu: ecuaciones e igualdades, resultados
    can: cantidad de barras
    desig: diccionario de designanciones de barra
    sit: TipoCarga, situacion a analizar
    cag: multiplos de fuerzas g
    pes: pesos por barra
    car: Lista con cargas si se ingresan manual.
    '''

    def __init__(
        self,
        incog: list,
        iba: list,
        ino: list,
        car: list,
        sop: list,
        conf: list,
        desig: dict[str, int],
        tipo: TipoCarga = 'n',
        cag: float = 0,
        pesos: list = None,
        pri=False,
        gra=False,
    ):
        self.conf = Conf(*conf)
        self.lso: list[Vinculo | None] = list()
        self.desig: dict[str, int] = desig
        self.sit: TipoCarga = tipo
        self.cag = cag
        self.pes: list[float] = pesos

        # Input nodos
        self.ctn = CtrN(ino)
        self.ctn.cargar()

        # cargo las barras
        self.ctb = CtrB(iba)
        self.ctb.cargar(self.ctn.lno, desig)

        # Controlador de graficos (Soportes)
        self.lso = list()
        for i in sop:
            self.cre_sop(i)

        # Controlador de ecuaciones(soluciona)
        self.sol = SolvIt(incog, self.sit, car)
        self.sol.carga(self.ctb.lis)
        self.sol.creas()
        self.sol.car_des(cag, tipo, self.ctb.lis, self.pes)
        self.sol.car_car()
        self.sol.cargi()
        self.sol.solvi()
        self.sol.solvi_bar(self.ctb.lis)
        self.sol.carga_bar(self.ctb.lis)
        self.ctb.cal()

        if pri:
            self.imprimi()

        self.graficar = gra

    def imprimi(self):

        hlp.col("Matriz de rigidez")
        print(self.sol.rig.to_string())

        hlp.col("Matriz de Fuerzas:")
        sp.pprint(self.sol.min)

        hlp.col("Matriz de desplazamiento:")
        sp.pprint(self.sol.mde)

        hlp.col("Soluciones:")
        lef = self.sol.ecu.lhs.tolist()
        for i, fila in enumerate(self.sol.ecu.rhs.tolist()):
            for j, val in enumerate(fila):
                print(f"{lef[i]}:{val:.3e}")

        for i in self.ctb.lis.values():
            hlp.col(f"Barra: {i.bar}")
            hlp.col(f"Matriz sistema global:")
            print(i.rgi.to_string())

            hlp.col(f"Esfuerzos:")
            sp.pprint(i.esf)

    def cre_sop(self, soi: list[int]):
        '''Funcion encargada de crear soporte

        Parameters
        ----------
        soi : list
            soporte individual a crearse y guardarse.
        '''
        tip: int
        nod: int
        ang: int

        tip = soi[0]
        nod = soi[1]
        ang = soi[2]

        nol = self.ctn.dtf.loc[nod]

        match tip:
            case 1:
                self.lso.append(ViculoPri(nol, ang))
            case 2:
                self.lso.append(ViculoSeg(nol, ang))
            case 3:
                self.lso.append(viculoTer(nol, ang))
            case _:
                pass

    def grf_est(self):
        gre = GrfEst(self.ctb.lis.values(), self.lso, self.conf)
        if self.graficar:
            gre.graficar()
            # gre.guardar(gre.fig, 'gre.png')
            gre.muestra()

    def grf_mom(self):
        grm = GrfMom(self.ctb.lis.values(), self.lso, self.conf)
        grm.cargado()
        if self.graficar:
            grm.graficar()
            grm.guardar(grm.fig, 'grm.pdf')
            grm.muestra()

    def grf_nor(self):
        grn = GrfNor(self.ctb.lis.values(), self.lso, self.conf)
        grn.cargado()
        if self.graficar:
            grn.graficar()
            grn.guardar(grn.fig, 'grn.pdf')
            grn.muestra()

    def grf_cor(self):
        grc = GrfCor(self.ctb.lis.values(), self.lso, self.conf)
        grc.cargado()
        if self.graficar:
            grc.graficar()
            grc.guardar(grc.fig, 'grc.pdf')
            grc.muestra()
