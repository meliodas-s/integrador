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
                # carga vertical
                self.vrl: sp.Symbol = sp.symbols('l')
                self.vrx: sp.Symbol = sp.symbols('x')
                vrq = self.dat
                self.mom = (
                    -vrq*self.vrl**2/12
                    + vrq*self.vrl*self.vrx/2
                    - self.vrx**2*vrq/2
                )

            case 2:
                # carga horizontal
                pass

            case 3:
                # carga triangular
                self.vrl: sp.Symbol = sp.symbols('l')
                self.vrx: sp.Symbol = sp.symbols('x')
                vrq = self.dat
                self.mom = (
                    -self.dat*self.vrl**2/20
                    + (7/20)*self.dat*self.vrl*self.vrx
                    - self.vrx**2*self.dat/2
                    + self.dat*self.vrx**3*(1/(2*self.vrl)-1/(3*self.vrl))
                )

class Carga0:
    vrl = sp.symbols('l')
    vrx = sp.symbols('x')
    dat = 0
    mom = 0