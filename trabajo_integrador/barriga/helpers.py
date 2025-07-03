import pandas as pd
import numpy as np
import sympy as sp
from IPython.display import display

def mrb(bar: pd.DataFrame, ino: pd.DataFrame, rig: pd.DataFrame, brc):
    '''Carga la matriz de rigiddez para cada barra.
    Dada la barra y la matriz de rigidez suma sus respectivo
    aporte en cada pocision.

    '''

    # indice de nodos
    noi = bar['noi']
    nof = bar['nof']

    # Indice de (nodo inicial momento, fuerx, fuery)
    nim = ino.loc[int(bar['noi']), 'imn']
    nix = ino.loc[int(bar['noi']), 'ifx']
    niy = ino.loc[int(bar['noi']), 'ify']

    # Indice de (nodo final momento, fuerx, fuery)
    nfm = ino.loc[int(bar['nof']), 'imn']
    nfx = ino.loc[int(bar['nof']), 'ifx']
    nfy = ino.loc[int(bar['nof']), 'ify']

    # Valores de lambdax y lambday
    lmx = bar['lmx']
    lmy = bar['lmy']

    # filas(indices)
    fid = [nix, niy, nim, nfx, nfy, nfm]

    # columnas(indices)
    cid = fid

    # Largo, area, inercia, elasticidad
    lar = bar['lar']
    are = bar['are']
    mod = bar['mod']
    ine = bar['ine']

    # Hay terminos repetirdos
    te1 = are*mod/lar
    te2 = 12*mod*ine/lar**3
    te3 = 6*mod*ine/lar**2
    te4 = 4*mod*ine/lar
    te5 = 2*mod*ine/lar

    # Matriz rigidez local de la barra (k`)
    mrl = (
        np.array(
            [
                [te1, 0, 0, -te1, 0, 0],
                [0, te2, te3, 0, -te2, te3],
                [0, te3, te4, 0, -te3, te5],
                [-te1, 0, 0, te1, 0, 0],
                [0, -te2, -te3, 0, te2, -te3],
                [0, te3, te5, 0, -te3, te4]
            ]
        )
    )

    # Matris de transformacion
    tra = (
        np.array(
            [
                [lmx, lmy, 0, 0, 0, 0],
                [-lmy, lmx, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, lmx, lmy, 0],
                [0, 0, 0, -lmy, lmx, 0],
                [0, 0, 0, 0, 0, 1]
            ]
        )
    )
    
    # Guardo la matriz de rigidex local
    brc.ril = mrl

    # Calculo la matriz de rigidez global (k) y guardo.
    brc.rig = (tra.T@mrl)@tra

    # Convierto (k) en df para coincidencia de indices.
    mrg = pd.DataFrame(brc.rig, index=fid, columns=cid)
    display(mrg)
    
    # Guardo datos de transpuesta.
    brc.tra = tra

    # Sumar los valores nuevos a la submatriz original
    sum = rig.loc[fid, cid].values + mrg
    rig.loc[fid, cid] = pd.DataFrame(sum, index=fid, columns=cid)

def col(text: str):
    print()
    print("\033[1;32m")
    print(text)
    print("\033[0m")
