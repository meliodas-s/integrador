from ..modu import Rock
import matplotlib.pyplot as plt
import sympy as sp
from plottable import Table


class Verificado:
    def __init__(self, rok: Rock):
        self.rok: Rock = rok
        self.lba = self.rok.lba
    
    def veri(self):
        for i in self.lba:
            print(i.bar)
            print(i.mom)
            print(i.cor)
            print(i.nor)
    
