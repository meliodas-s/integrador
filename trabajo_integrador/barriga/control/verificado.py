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
            'Anec[m^2]',         # 4
            'Wnec[m^3]',         # 5
            'Denom[]',        # 6
            't',            # 7
            'ag',           # 8
            'wcal',         # 9
            'ical',         # 10
            'mcal',         # 11
            r'\sigma',      # 12
            r'\tau',        # 13
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
                self.mve.at[inx, col[0]] = rdx
                self.mve.at[inx, col[1]] = round(i.nor.subs({i.vrx: rdx}),3)
                self.mve.at[inx, col[2]] = round(i.cor.subs({i.vrx: rdx}),3)
                self.mve.at[inx, col[3]] = round(i.mom.subs({i.vrx: rdx}),3)
        
        self.mve[col[4]] = np.round(np.abs(self.mve[col[1]]/self.rca),3)
        self.mve[col[5]] = np.round(np.abs(self.mve[col[3]]/self.rca),3)
        

        print(self.mve.round(2).to_string())