import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes


class Grafica:
    pass

    def configraf(self, ax: Axes, spcmin, tit, mix, max, miy, may, fig, spc, xlb, ylb):
        '''Me configura y grafica la grafica'''

        # Configuraciones para figura
        ax.legend()
        ax.set_aspect('equal')
        ax.set_xticks(np.arange(int(mix)-1, int(max)+1, spc))
        ax.set_yticks(np.arange(int(miy)-1, int(may)+1, spc))
        ax.set_xticks(np.arange(int(mix)-1, int(max)+1, spcmin), minor=True)
        ax.set_yticks(np.arange(int(miy)-1, int(may)+1, spcmin), minor=True)

        # grid menores
        ax.grid(
            True,
            which='major',
            linestyle='-',
            linewidth=0.5,
            alpha=0.5,
            color='black')
        ax.grid(
            True,
            which='minor',
            linestyle='--',
            linewidth=0.4,
            alpha=0.5,
            color='black')

        # Miselaneos
        ax.set_ylim(miy, may)
        ax.set_xlim(mix, max)
        ax.set_xlabel(xlb)
        ax.set_ylabel(ylb)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax.set_title(tit)
        ax.set_facecolor('#EACEC4')
        ax.set_axisbelow(True)
        fig.patch.set_facecolor('#EACEC4')

        # eliminar etiquetas duplicadas
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(
            dict(zip(labels, handles)).values(),
            dict(zip(labels, handles)).keys()
        )

        ax.tick_params(axis='x', labelrotation=60)  # Eje x
        ax.tick_params(axis='both', labelsize=7)  # Cambia tamaño en ambos ejes

    def guardar(self, fig, nombre):
        fig.set_size_inches(15, 15)
        fig.savefig(
            nombre,
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.2,
            format='png',
        )
