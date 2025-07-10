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
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import Optional
from adjustText import adjust_text
from copy import deepcopy


class GrfEsf(Grafica):
    def __init__(self, lba: list[Barra], lso, con: Conf):
        super().__init__()
        self.con = con
        self.lba = lba
        self.lso = lso
        self.est = GrfEst(self.lba, self.lso, con)
        self.tgr = []
        self.tit = ""
        self.axe: Optional[Axes] = None
        self.fig: Optional[Figure] = None
        self.txs: Optional[list] = list()
        self.ctx: Optional[list] = list()

    def graficar(self):
        self.est.graficar(False)
        self.axe = self.est.axe
        self.fig = self.est.fig
        vrx = sp.symbols('x')

        # Creo un cero simbolico
        ces = sp.Mul(vrx, 0, evaluate=False)

        # grafico los momenots
        for i in self.tgr:
            # Se convierte la expresion
            f_lambdified = sp.lambdify(
                vrx,
                (i[1] + ces),
                'numpy'
            )
            x_vals = np.linspace(0, i[0].lar, 500)
            y_vals = f_lambdified(x_vals)
            self.axe.fill_between(
                x_vals,
                y_vals,
                alpha=0.3,
                transform=i[2] + self.axe.transData,
                zorder=19,
                ec = 'black',
                lw=0.7
            )
            self.axe.plot(
                x_vals,
                y_vals,
                alpha=0.9,
                transform=i[2] + self.axe.transData,
                zorder=19,
                color = 'black',
                lw=0.6
            )


            # graficar minimos maximos y ceros
            self.grafmax(
                self.axe,
                np.round(x_vals, 4),
                np.round(y_vals, 4),
                i[2])

        x = list()
        y = list()
        for i in self.ctx:
            x.append(i[0])
            y.append(i[1])

        # creo copia y ajusto el texto
        adjust_text(
            self.txs,
            x=x,
            y=y,
            expand=(2, 3),
            expand_text=(2, 3),
            explode_radius = 1000,
            force_explode = (0.6,0.9),
            force_text=(1, 20),
            max_move=(50, 50),
            only_move = {"explode": "xy","text": "xy"}
            # iter_lim=300,
            # time_lim=15,   
        )

        # Dibujar manualmente las flechas desde el texto movido al punto original
        for i, txt in enumerate(self.txs):
            # Coordenadas del texto ajustado
            xt, yt = txt.get_position()

            # Coordenadas originales
            xo, yo = self.ctx[i]

            # Dibujar la flecha
            self.axe.annotate(
                "",
                zorder=40,
                xy=(xo, yo),
                xytext=(xt, yt),
                arrowprops=dict(
                    arrowstyle="->",
                    color="black",
                    lw=0.65,
                    alpha=0.7
                )
            )

        # configurar grafica
        self.configraf(
            self.axe,
            0.5,
            self.tit,
            self.con.xmin,
            self.con.xmax,
            self.con.ymin,
            self.con.ymax,
            self.fig,
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
        myt = (
            Affine2D()
            .scale(1, esc)
            .rotate(ara)
            .translate(bar.xin, bar.yin)
        )
        return myt

    def grafmax(self, axe, xva, yva, tra):
        fsz = 8
        orderz = 20
        precis = 4

        # Calculo minimo, maximo y cerps
        orden = 5
        max_idx = argrelextrema(yva, np.greater, order=orden)[0]
        min_idx = argrelextrema(yva, np.less, order=orden)[0]
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

            # graficar cada cero
            for i in chs:
                x_t, y_t = tra.transform_point((xva[i], yva[i]))
                axe.plot(
                    x_t,
                    y_t,
                    'bo',
                    label='Ceros',
                    markersize=1.5
                )
                txt = axe.text(
                    x_t,
                    y_t,
                    f"{xva[i]:.{precis}}[m]",
                    color='black',
                    fontsize=fsz,
                    ha='center',
                    zorder=orderz,
                    bbox=dict(
                        facecolor='green',
                        alpha=0.3,
                        edgecolor='none',
                        boxstyle='round')
                )
                self.txs.append(txt)
                self.ctx.append(txt.get_position())

        # Si tiene min o max los grafica
        if min_idx.size != 0:

            # Marcar minimo
            x_t, y_t = tra.transform_point((xva[min_idx][0], yva[min_idx][0]))
            axe.plot(x_t, y_t, 'bo', label='Minimo', markersize=1.5)
            txt = axe.text(
                x_t,
                y_t,
                f"{yva[min_idx][0]}",
                color='black',
                fontsize=fsz,
                ha='center',
                zorder=orderz,
                bbox=dict(
                    facecolor='blue',
                    alpha=0.3,
                    edgecolor='none',
                    boxstyle='round')
            )
            self.txs.append(txt)
            self.ctx.append(txt.get_position())

        if max_idx.size != 0:
            # Marcar máximo
            x_t, y_t = tra.transform_point((xva[max_idx][0], yva[max_idx][0]))
            axe.plot(x_t, y_t, 'ro', label='Maximo', markersize=1.5)
            txt = axe.text(
                x_t,
                y_t,
                f"{yva[max_idx][0]:.{precis}}",
                color='black',
                fontsize=fsz,
                ha='center',
                zorder=orderz,
                bbox=dict(
                    facecolor='red',
                    alpha=0.3,
                    edgecolor='none',
                    boxstyle='round')
            )
            self.txs.append(txt)
            self.ctx.append(txt.get_position())

        # Letra de extemos offsets en x e y
        bbx = dict(
            facecolor='white',
            alpha=0.6,
            edgecolor='none',
            boxstyle='round')
        if math.fabs(yva[-1]) > 1:
            x_t, y_t = tra.transform_point((xva[-1], yva[-1]))
            txt = axe.text(
                x_t,
                y_t,
                f"{yva[-1]:.{precis}}",
                color='black',
                fontsize=fsz,
                ha='center',
                zorder=orderz,
                bbox=bbx
            )
            self.txs.append(txt)
            self.ctx.append(txt.get_position())

        # Letra de extemos offsets en x e y
        if math.fabs(yva[0]) > 1:
            x_t, y_t = tra.transform_point((xva[0], yva[0]))
            txt = axe.text(
                x_t,
                y_t,
                f"{yva[0]:.{precis}}",
                color='black',
                fontsize=fsz,
                ha='center',
                zorder=orderz,
                bbox=bbx
            )
            self.txs.append(txt)
            self.ctx.append(txt.get_position())


class GrfMom(GrfEsf):
    def __init__(self, lba, lso, conf: Conf):
        super().__init__(lba, lso, conf)
        self.tit = f'Momento $1[m]={self.con.escm:.4}[N\\cdot m]$'

    def cargado(self):
        for i in self.lba:
            tr = self.transfo(i, -self.con.escm)
            li = [i, i.mom, tr]
            self.tgr.append(li)


class GrfNor(GrfEsf):
    def __init__(self, lba, lso, conf: Conf):
        super().__init__(lba, lso, conf)
        self.tit = f'Normal $1[m]={self.con.escn:.4}[N]$'

    def cargado(self):
        for i in self.lba:
            tr = self.transfo(i, self.con.escn)
            li = [i, i.nor, tr]
            self.tgr.append(li)


class GrfCor(GrfEsf):
    def __init__(self, lba, lso, conf: Conf):
        super().__init__(lba, lso, conf)
        self.tit = f'Cortante $1[m]={self.con.escq:.4}[N]$'

    def cargado(self):
        for i in self.lba:
            tr = self.transfo(i, self.con.escq)
            li = [i, i.cor, tr]
            self.tgr.append(li)
