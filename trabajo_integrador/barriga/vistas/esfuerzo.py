from .grafica import Grafica
from .estructura import GrfEst
import matplotlib.pyplot as plt
import sympy as sp
from matplotlib.transforms import Affine2D
from ..modelos.barra import Barra
import numpy as np
import math
from ..modelos.config import Conf
from scipy.signal import argrelextrema


class GrfEsf(Grafica):
    def __init__(self, lba, lso, con: Conf):
        super().__init__()
        self.con = con
        self.lba = lba
        self.lso = lso
        self.est = GrfEst(self.lba, self.lso, con)
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
                (i[1] + ces).evalf(4),
                'numpy'
            )
            x_vals = np.linspace(0, i[0].lar, 500)
            y_vals = f_lambdified(x_vals)
            axe.fill_between(
                x_vals,
                y_vals,
                alpha=0.7,
                transform=i[2] + axe.transData
            )

            # graficar minimos maximos y ceros
            self.grafmax(axe, x_vals, y_vals, i[2])

            # configurar grafica
            tit = f'Momento $1[m]={self.con.escm:.4}[N\cdot m]$'
            self.configraf(
                axe,
                0.5,
                tit,
                self.con.xmin,
                self.con.xmax,
                self.con.ymin,
                self.con.ymax,
                fig,
                1,
                'x[m]',
                'y[m]'
            )

    def muestra(self):
        plt.show()

    def transfo(self, bar: Barra, esc):
        # se calcula el angulo
        dx = bar.xfi - bar.xin
        dy = bar.yfi - bar.yin
        ara = math.atan2(dy, dx)

        # Se crea la transformacion
        print(math.degrees(math.acos(bar.lmx)))
        myt = (
            Affine2D()
            .scale(1, esc)
            # .rotate(math.acos(bar.lmx))
            .rotate(ara)
            .translate(bar.xin, bar.yin)
        )
        return myt

    def grafmax(self, axe, xva, yva, tra):
        fsz = 8

        # Calculo minimo y maximo
        orden = 5
        max_idx = argrelextrema(yva, np.greater, order=orden)[0]
        min_idx = argrelextrema(yva, np.less, order=orden)[0]

        # Calculo de 0 (change sign)
        chs = np.where(np.diff(np.sign(yva)))[0]

        # Si tiene cero los grafica
        if chs.size != 0:
            chs2 = []
            for i in chs:
                if i == 0:
                    continue
                else:
                    chs2.append(i)
            chs = chs2

            # Marcar minimo
            x_t, y_t = tra.transform_point((xva[chs][0], yva[chs][0]))
            axe.plot(x_t, y_t, 'bo', label='Ceros', markersize=1.5)
            axe.text(
                x_t,
                y_t-0.01,
                f"{xva[chs][0]:.3}[m]",
                color='black',
                fontsize=fsz,
                ha='center',
                bbox=dict(
                    facecolor='green',
                    alpha=0.4,
                    edgecolor='none',
                    boxstyle='round')
            )

        # Si tiene min o max los grafica
        if min_idx.size != 0:

            # Marcar minimo
            x_t, y_t = tra.transform_point((xva[min_idx][0], yva[min_idx][0]))
            axe.plot(x_t, y_t, 'bo', label='Minimo', markersize=1.5)
            axe.text(
                x_t,
                y_t-0.01,
                f"{yva[min_idx][0]}",
                color='black',
                fontsize=fsz,
                ha='center',
                bbox=dict(
                    facecolor='blue',
                    alpha=0.4,
                    edgecolor='none',
                    boxstyle='round')
            )

        if max_idx.size != 0:
            # Marcar máximo
            x_t, y_t = tra.transform_point((xva[max_idx][0], yva[max_idx][0]))
            axe.plot(x_t, y_t, 'ro', label='Maximo', markersize=1.5)
            axe.text(
                x_t,
                y_t-0.01,
                f"{yva[max_idx][0]:.3}",
                color='black',
                fontsize=fsz,
                ha='center',
                bbox=dict(
                    facecolor='red',
                    alpha=0.4,
                    edgecolor='none',
                    boxstyle='round')
            )

        # Letra de extemos offsets en x e y
        bbx = dict(
            facecolor='white',
            alpha=0.6,
            edgecolor='none',
            boxstyle='round')
        if math.fabs(yva[-1]) > 10:
            x_t, y_t = tra.transform_point((xva[-1], yva[-1]))
            axe.text(
                x_t,
                y_t-0.01,
                f"{yva[-1]:.3}",
                color='black',
                fontsize=fsz,
                ha='center',
                bbox=bbx
            )

        # Letra de extemos offsets en x e y
        if math.fabs(yva[0]) > 10:
            x_t, y_t = tra.transform_point((xva[0], yva[0]))
            axe.text(
                x_t,
                y_t-0.01,
                f"{yva[0]:.3}",
                color='black',
                fontsize=fsz,
                ha='center',
                bbox=bbx
            )


class GrfMom(GrfEsf):
    def __init__(self, lba, lso, conf: Conf):
        super().__init__(lba, lso, conf)

    def cargado(self):
        # to_graf
        self.tgr = list()

        for i in self.lba:
            tr = self.transfo(i, -self.con.escm)
            li = [i, i.mom, tr]
            self.tgr.append(li)
