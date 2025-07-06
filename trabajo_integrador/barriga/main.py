from .modu import Rock
import matplotlib.pyplot as plt
from plottable import Table
import pandas as pd
import copy

from .ejemplos import ejemplo2 as ejemplo

# Se cargan los datos
inc = ejemplo['inc']
iba = ejemplo['iba']
ino = ejemplo['ino']
car = ejemplo['car']
sop = ejemplo['sop']

# Se crea la estructura
acdc = Rock(inc, iba, ino, car, sop,pri=True)

acdc.grf_est()
acdc.grf_mom()
