import numpy as np

class Grafica:
    pass

    def configraf(self, ax, spcmin, tit, mix, max, miy, may, fig, spc):
        '''Me configura y grafica la grafica'''

        # Configuraciones para figura
        ax.legend()
        ax.set_aspect('equal')
        ax.set_xticks(np.arange(mix, max, spc))
        ax.set_yticks(np.arange(miy, may, spc))
        ax.set_xticks(np.arange(mix, max, spcmin), minor=True)
        ax.set_yticks(np.arange(miy, may, spcmin), minor=True)

        # Grid menores
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
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax.set_title(tit)
        ax.set_facecolor('#EACEC4')
        ax.set_axisbelow(True)
        fig.patch.set_facecolor('#EACEC4')