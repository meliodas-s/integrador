import pandas as pd
import numpy as np
import sympy as sp
from IPython.display import display


def mrb(bar, rig: pd.DataFrame):
    '''Carga la matriz de rigiddez para cada barra.
    Dada la barra y la matriz de rigidez suma sus respectivo
    aporte en cada pocision.
    '''
    # filas(indices) de momentos, fuerx, fuery
    fid = [bar.nix, bar.niy, bar.nim, bar.nfx, bar.nfy, bar.nfm]

    # columnas(indices)
    cid = fid

    # Convierto (k) en df para coincidencia de indices.
    mrg = pd.DataFrame(bar.rig, index=fid, columns=cid)

    # Sumar los valores nuevos a la submatriz original
    sum = rig.loc[fid, cid].values + mrg
    rig.loc[fid, cid] = pd.DataFrame(sum, index=fid, columns=cid)


def col(text: str):
    print()
    print("\033[1;32m")
    print(text)
    print("\033[0m")
