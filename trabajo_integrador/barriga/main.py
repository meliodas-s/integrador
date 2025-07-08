from .modu import Rock
from .control.impresion import Impresion
from .control.verificado import Verificado
import matplotlib.pyplot as plt
from plottable import Table
import pandas as pd
import copy

from .ejemplos.ejemplo4 import datos as ejemplo

# Parametros
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern']
plt.rcParams['text.latex.preamble'] = r'''
\usepackage{amsmath}
\usepackage{textgreek}
'''


# Se cargan los datos
inc = ejemplo['inc']
iba = ejemplo['iba']
ino = ejemplo['ino']
car = ejemplo['car']
sop = ejemplo['sop']
con = ejemplo['con']
desig = ejemplo['desig']

# Se crea la estructura
mod = Rock(inc, iba, ino, car, sop,con, desig, pri=False)

mod.grf_est()
mod.grf_mom()
mod.grf_cor()
mod.grf_nor()

# modulo para imprimir matrices
imp = Impresion(mod)
imp.desp()
imp.fuer()
imp.rigi()
imp.incs()
imp.barr()
imp.barg()

# modulo de verificado
ver = Verificado(mod)
ver.veri()
ver.impr()
