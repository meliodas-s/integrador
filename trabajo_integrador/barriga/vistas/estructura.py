import matplotlib.pyplot as plt
import numpy as np
from ..modelos.barra import Barra
from .grafica import Grafica
from ..modelos.config import Conf


class GrfEst(Grafica):
    def __init__(self, lba: list[Barra], lso, conf:Conf):
        self.lba = lba
        self.lso = lso
        self.con = conf

    def graficar(self, config=True):
        # lienzo
        fig, ax = plt.subplots(figsize=(20,20))
        self.fig = fig
        self.axe = ax
        # barras
        for i in self.lba:
            ax.plot(
                [i.noi.cox, i.nof.cox], [i.noi.coy, i.nof.coy],
                linewidth=4,
                color='gray',
                alpha=0.7
            )
            ax.plot(
                [i.noi.cox, i.nof.cox], [i.noi.coy, i.nof.coy],
                linewidth=1.5,
                color='gray',
                alpha=0.9
            )

        # soporte
        for so in self.lso:
            so.print(ax)

        if config:
            tit = 'Estructura'
            self.configraf(
                ax, 
                0.5,
                tit, 
                self.con.xmin, 
                self.con.xmax,
                self.con.ymin,
                self.con.ymax,
                fig,
                1,
                'x[m]',
                'y[m]')

    def muestra(self):
        plt.show()

    def transformar(self):
        pass
