import pandas as pd

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
    
    if True:
            col(f"Matriz de B{bar.bar}")
            print(mrg.to_string())
            print(bar.lar)


    # Sumar los valores nuevos a la submatriz original
    sum = rig.loc[fid, cid].values + mrg
    rig.loc[fid, cid] = pd.DataFrame(sum, index=fid, columns=cid)


def col(text: str):
    print()
    print("\033[1;32m")
    print(text)
    print("\033[0m")
