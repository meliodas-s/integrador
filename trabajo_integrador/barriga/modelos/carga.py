import sympy as sp


class Carga:
    def __init__(self, bar: int, tip: int, dat: int):
        self.bar = bar
        self.tip = tip
        self.dat = dat
        
        self.cal_ecu()

    def cal_ecu(self):
        '''Calcula la ecuacion correspondiente.
        '''

        match self.tip:
            case 1:
                # Carga lineal
                self.vrl:sp.Symbol = sp.symbols('l')
                self.vrx:sp.Symbol = sp.symbols('x')
                vrq = self.dat
                print(vrq)
                self.mom = (
                    -vrq*self.vrl**2/12
                    + vrq*self.vrl*self.vrx/2
                    - self.vrx**2*vrq/2
                )
            case 2:
                # Carga triangular
                pass
