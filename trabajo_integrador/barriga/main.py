from .modu import Rock
import matplotlib.pyplot as plt
from plottable import Table
import pandas as pd
import copy

# Fuerzas
inc = [
    # 1
    [0, False],

    # 2
    [0, False],

    # 3
    [0, True],

    # 4
    [-25e3, True],

    # 5
    [13.5, True],

    # 6
    [0, False],

    # 7
    [0, False],

    # 8
    [0, False],

    # 9
    [0, False],

    # 10
    [0, False],

    # 11
    [0, True],

    # 12
    [62.5e3, True],

    # 13
    [-50e3, True],

    # 14
    [0, True],

    # 15
    [-83.333e3, True],

    # 16
    [0, False],

    # 17
    [0, False],

    # 18
    [0, False],
    
    # 19
    [0, False],
    
    # 20
    
    [0, False],

]

# bar,noi,nof,are,mod,iner (m, N)
iba = [
    [1, 1, 2, 0.1, 2000, 0.1],
    [2, 3, 2, 0.1, 2000, 0.1],
    [3, 2, 4, 0.1, 2000, 0.1],
    [4, 4, 5, 0.1, 2000, 0.1],
    [5, 5, 6, 0.1, 2000, 0.1]
]

# nod,imn,ifx,ify,cox,coy
ino = [
    [1, 3, 2, 1, 0, 0],
    [2, 6, 5, 4, 5, 3],
    [3, 9, 8, 7, 5, 0],
    [4, 12, 11, 10, 10, 3],
    [5, 15, 14, 13, 20, 3],
    [6, 18, 17, 16, 20, 1]
]

# Cargas (bar, (1:ver, 2:hor ,3:tri), q)
car = [
    [2, 3, 30e3],
    [3, 1, 10e3],
    [4, 1, 10e3],
]

acdc = Rock(inc, iba, ino, car, pri=False)

# acdc.grf_est()
