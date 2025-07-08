from ..modu import Rock
import matplotlib.pyplot as plt
import sympy as sp
from plottable import Table


class Impresion:

    def __init__(self, rok: Rock, res=250):
        self.rok: Rock = rok
        self.res: int = res

    def desp(self):
        # texto de la matriz de desplazamiento
        ltx = sp.latex(self.rok.mde)

        # Init a figure
        fig, ax = plt.subplots(figsize=(2, 1))
        ax.text(0, 0.5, r'$\fbox{Desplazamientos}$', ha='center', va='bottom')
        ax.text(0, 0, r'\[%s\]' % ltx, ha='center', va='top')

        # Configuraciones para figura
        ax.set_facecolor('#EACEC4')
        ax.set_xlim([-1, 1])
        fig.patch.set_facecolor('#EACEC4')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')

        # Display the output
        fig.savefig('des.png', bbox_inches='tight', dpi=self.res)

    def fuer(self):
        # texto de la matriz de fuerzas
        ltx = sp.latex(self.rok.min)

        # Init a figure
        fig, ax = plt.subplots(figsize=(2, 1))
        ax.text(0, 0.5, r'$\fbox{Fuerza}$', ha='center', va='bottom')
        ax.text(0, 0, r'\[%s\]' % ltx, ha='center', va='top')

        # Configuraciones para figura
        ax.set_facecolor('#EACEC4')
        ax.set_xlim([-1, 1])
        fig.patch.set_facecolor('#EACEC4')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')

        # Display the output
        fig.savefig('fue.png', bbox_inches='tight', dpi=self.res)

    def rigi(self):
        # Init a figure
        fig, ax = plt.subplots(figsize=(23, 9))

        dff = self.rok.rig.applymap(
            lambda x: f"{x:.4}" if isinstance(x, (float, int)) else x)

        # Configuraciones para figura
        ax.set_title(r'$\fbox{Matriz de rigidez global}$')
        ax.set_facecolor('#EACEC4')
        ax.set_axisbelow(True)
        fig.patch.set_facecolor('#EACEC4')
        ax.axis('off')

        # Configuraciones para figura
        # tab = Table(self.rok.rig.round(4), ax)
        tab = Table(dff, ax)

        # Display the output
        fig.savefig('rig.png', bbox_inches='tight', dpi=self.res)

    def incs(self):
        # texto de la matriz incognitas
        ltx = sp.latex(self.rok.ecu.evalf(4))

        # Init a figure
        fig, ax = plt.subplots(figsize=(2, 1))
        ax.text(0, 0.5, r'$\fbox{Incognitas}$', ha='center', va='bottom')
        ax.text(0, 0, r'\[%s\]' % ltx, ha='center', va='top')

        # Configuraciones para figura
        ax.set_facecolor('#EACEC4')
        ax.set_xlim([-1, 1])
        fig.patch.set_facecolor('#EACEC4')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')

        # Display the output
        fig.savefig('inc.png', bbox_inches='tight', dpi=self.res)

    def barg(self):
        # imprime las matrices de rigidez de cada barra
        for i in self.rok.lba:
            fig, ax = plt.subplots(figsize=(9, 9))

            # Configuraciones para figura
            ax.set_title(r'$\fbox{Matriz global}$')
            ax.set_facecolor('#EACEC4')
            ax.set_axisbelow(True)
            fig.patch.set_facecolor('#EACEC4')
            ax.axis('off')

            # Configuraciones para figura
            tab = Table(i.rgi.round(2), ax)

            # Display the output
            fig.savefig(f'sld_ba{i.bar}_a.png', bbox_inches='tight', dpi=self.res)

    def barr(self):
        for i in self.rok.lba:
            bid = i.bar
            tit = r'$\fbox{Barra %s}$' % bid

            lt2 = sp.latex(i.mom)
            lt3 = sp.latex(i.cor)
            lt4 = sp.latex(i.nor)

            # Init a figure
            txt = "Las valores de x[m] son de desde 0 hasta el final de la barra."
            fig, ax = plt.subplots(figsize=(2, 1))
            ax.text(0, 0, tit, ha='center', va='bottom')
            ax.text(0, -1, txt, ha='center', va='top')
            ax.text(0, -2, r'\fbox{Esfuerzo de momento}',
                    ha='center', va='top')
            ax.text(0, -3, r'\[%s\]' % lt2, ha='center', va='top')
            ax.text(0, -4, r'\fbox{Esfuerzo de corte}', ha='center', va='top')
            ax.text(0, -5, r'\[%s\]' % lt3, ha='center', va='top')
            ax.text(0, -6, r'\fbox{Esfuerzo de normal}',
                    ha='center', va='top')
            ax.text(0, -7, r'\[%s\]' % lt4, ha='center', va='top')

            # Configuraciones para figura
            ax.set_facecolor('#EACEC4')
            ax.set_xlim([-1, 1])
            fig.patch.set_facecolor('#EACEC4')
            ax.set_xticks([])
            ax.set_yticks([])
            ax.axis('off')

            # Display the output
            fig.savefig(f'sld_ba{bid}_b.png', bbox_inches='tight', dpi=self.res)
