from .grafica import Grafica
from .estructura import GrfEst
import matplotlib.pyplot as plt


class GrfEsf(Grafica):
    def __init__(self, lba, lso):
        super().__init__()
        self.lba = lba
        self.lso = lso
        self.est = GrfEst(self.lba, self.lso)
    
    def graficar(self):
        self.est.graficar()
    
    def muestra(self):
        plt.show()




class GrfMom(GrfEsf):
    def __init__(self, lba, lso):
        super().__init__(lba, lso)
    
    def cargado(self):
        # to_graf
        self.tgr = list()

        for i in self.lba:
            li = [i, i.mom]
            self.tgr.append(li)
