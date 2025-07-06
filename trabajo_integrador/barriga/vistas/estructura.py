import matplotlib.pyplot as plt
import numpy as np
from ..modelos.barra import Barra
from .grafica import Grafica


class GrfEst(Grafica):
    def __init__(self, lba: list[Barra], lso):
        self.lba = lba
        self.lso = lso

    def graficar(self):
        # lienzo
        fig, ax = plt.subplots()
        self.fig = fig
        self.axe = ax
        # barras
        for i in self.lba:
            ax.plot(
                [i.xin, i.xfi], [i.yin, i.yfi],
                linewidth=2,
                color='gray',
                alpha=0.9
            )

        # soporte
        for so in self.lso:
            so.print(ax)

        self.configraf(ax, 0.5, '', -4, 25, -4, 5, fig, 1)

    def muestra(self):
        plt.show()

    def transformar(self):
        pass
