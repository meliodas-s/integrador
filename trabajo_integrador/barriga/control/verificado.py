from ..modu import Rock
import matplotlib.pyplot as plt
import sympy as sp
from plottable import Table
import pandas as pd
import numpy as np

class Verificado:
    def __init__(self, rok: Rock):
        self.rok: Rock = rok
        self.idx: list[str] = list()
        self.indi()
        self.col: list[str] = [
            'x',            # 0
            'N',            # 1
            'Q',            # 2
            'M',            # 3
            '$A_{nec}[m^2]$',         # 4
            '$W_{nec}[m^3]$',         # 5
            'Denom',        # 6
            't[m]',            # 7
            '$A_{cal}[m^2]$',           # 8
            '$W_{cal}[m^3]$',         # 9
            '$I_{cal}[m^4]$',         # 10
            '$m_{cal}[m^3]$',         # 11
            r'$\sigma$',      # 12
            r'$\tau$',        # 13
        ]
        self.lba = self.rok.lba
        self.mve: pd.DataFrame = pd.DataFrame(
            0,
            index=self.idx,
            columns=self.col
        )
        
        # coeficiente parcial segun material
        self.cps = 1.05
        
        # tension limite elastico (N/m2)
        self.tle = 225e6
        
        # resiste calculo
        self.rca = self.tle/self.cps
        
        # resitencia calculo tangencial
        self.rct = self.rca/(3**(1/3))

    def indi(self):
        for i in self.rok.lba:
            for j in range(4):
                self.idx.append(f'Barra{i.bar}-Punto{j}')

    def veri(self):
        col = self.col
        for i in self.lba:
            print(i.bar)
            print(i.mom)
            print(i.cor)
            print(i.nor)
            for j in range(4):

                # reemplazdo de x
                rdx = i.lar*j/3

                # indice en la matriz
                inx = f'Barra{i.bar}-Punto{j}'

                # cargado
                self.mve.at[inx, col[0]] = round(rdx,3)
                self.mve.at[inx, col[1]] = np.float64(i.nor.subs({i.vrx: rdx}))
                self.mve.at[inx, col[2]] = np.float64(i.cor.subs({i.vrx: rdx}))
                self.mve.at[inx, col[3]] = np.float64(i.mom.subs({i.vrx: rdx}))
                self.mve.at[inx, col[6]] = i.desig['nombre']
                self.mve.at[inx, col[7]] = 2*i.desig['tf']
                self.mve.at[inx, col[8]] = 2*i.desig['ag']
                self.mve.at[inx, col[9]] = 2*i.desig['sx']
                self.mve.at[inx, col[10]] = 2*i.desig['ix']
                self.mve.at[inx, col[11]] = 2*i.desig['qx']
        
        self.mve[col[4]] = np.abs(self.mve[col[1]]/self.rca).map(lambda x: np.float64(x))
        self.mve[col[5]] = np.abs(self.mve[col[3]]/self.rca).map(lambda x: np.float64(x))
        
        # sigma
        self.mve[col[12]] = (
            np.abs(self.mve[col[1]]/self.mve[col[8]])
            +np.abs(self.mve[col[3]]/self.mve[col[9]])
            )
        self.mve[col[13]] = np.abs(
            self.mve[col[2]]*self.mve[col[11]]/
            (self.mve[col[7]]*self.mve[col[10]])
            )
        

        # verifico tau
        self.mve[r'$\tau$ verifica'] = 'no cumple'
        self.mve.loc[self.rct > self.mve[col[13]], r'$\tau$ verifica'] = 'cumple'
        
        # verifico sigma
        self.mve[r'$\sigma$ verifica'] = 'no cumple'
        self.mve.loc[self.rca > self.mve[col[12]] , r'$\sigma$ verifica'] = 'cumple'
        
        #
        self.mve[col[1]]= self.mve[col[1]].map(lambda x: f"{x:.4}")
        self.mve[col[2]]= self.mve[col[2]].map(lambda x: f"{x:.4}")
        self.mve[col[3]]= self.mve[col[3]].map(lambda x: f"{x:.4}")
        self.mve[col[4]]= self.mve[col[4]].map(lambda x: f"{x:.4}")
        self.mve[col[5]]= self.mve[col[5]].map(lambda x: f"{x:.4}")
        self.mve[col[12]]= self.mve[col[12]].map(lambda x: f"{x:.4}")
        self.mve[col[13]]= self.mve[col[13]].map(lambda x: f"{x:.4}")

        print(self.mve)
        
    def impr(self):
        # Init a figure
        fig, ax = plt.subplots(figsize=(20, 9))
        

        # Configuraciones para figura
        ax.set_title(r'$\fbox{Matriz de verificacion}$')
        ax.set_facecolor('#EACEC4')
        ax.set_axisbelow(True)
        fig.patch.set_facecolor('#EACEC4')
        ax.axis('off')

        # Configuraciones para figura
        tab = Table(self.mve, ax)

        # Display the output
        fig.savefig('sld_mve.png', bbox_inches='tight', dpi=200)