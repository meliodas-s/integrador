from .grafica import Grafica
from .estructura import GrfEst
import matplotlib.pyplot as plt
import sympy as sp
from matplotlib.transforms import Affine2D
from ..modelos.barra import Barra
import numpy as np
import math


class GrfEsf(Grafica):
    def __init__(self, lba, lso, esc):
        super().__init__()
        self.esc = esc
        self.lba = lba
        self.lso = lso
        self.est = GrfEst(self.lba, self.lso)
        self.tgr = [] 

    def graficar(self):
        self.est.graficar()
        axe = self.est.axe
        fig = self.est.fig
        vrx = sp.symbols('x')

        # Creo un cero simbolico
        ces = sp.Mul(1, 0, evaluate=False)

        # grafico los momenots
        for i in self.tgr:
            # Se convierte la expresion
            f_lambdified = sp.lambdify(
                vrx,
                i[1] + ces,
                'numpy'
            )
            x_vals = np.linspace(0, i[0].lar, 15)
            y_vals = f_lambdified(x_vals)
            axe.fill_between(
                x_vals,
                y_vals,
                alpha=0.7,
                transform=i[2] + axe.transData
            )

    def muestra(self):
        plt.show()

    def transfo(self, bar:Barra ,esc):
        # se calcula el angulo
        dx = bar.xfi - bar.xin
        dy = bar.yfi - bar.yin
        ara = math.atan2(dy, dx)

        # Se crea la transformacion
        print(math.degrees(math.acos(bar.lmx)))
        myt = (
            Affine2D()
            .scale(1,esc)
            # .rotate(math.acos(bar.lmx))
            .rotate(ara)
            .translate(bar.xin, bar.yin)
        )
        return myt


class GrfMom(GrfEsf):
    def __init__(self, lba, lso, esc):
        super().__init__(lba, lso, esc)

    def cargado(self):
        # to_graf
        self.tgr = list()

        for i in self.lba:
            tr = self.transfo(i, -self.esc)
            li = [i, i.mom, tr]
            self.tgr.append(li)
