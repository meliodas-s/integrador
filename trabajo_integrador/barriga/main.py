from .modu import Rock
import matplotlib.pyplot as plt
from plottable import Table
import pandas as pd
import copy

from .ejemplos import ejemplo2 as ejemplo

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

# Se crea la estructura
acdc = Rock(inc, iba, ino, car, sop,con,pri=True)

acdc.grf_est()
acdc.grf_mom()
