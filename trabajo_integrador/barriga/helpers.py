import pandas as pd
from .modelos.barra import Barra

def mrb(bar:Barra, rig: pd.DataFrame):
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
    
    # guarda la matriz indexda
    bar.rgi = mrg

    # Sumar los valores nuevos a la submatriz original
    sum = rig.loc[fid, cid].values + mrg
    rig.loc[fid, cid] = pd.DataFrame(sum, index=fid, columns=cid)


def col(text: str, color: str='green'):
    colors = {
        "black":   "\033[30m",
        "red":     "\033[31m",
        "green":   "\033[32m",
        "yellow":  "\033[33m",
        "blue":    "\033[34m",
        "magenta": "\033[35m",
        "cyan":    "\033[36m",
        "white":   "\033[37m"
    }

    bg_colors = {
        "black":   "\033[40m",
        "red":     "\033[41m",
        "green":   "\033[42m",
        "yellow":  "\033[43m",
        "blue":    "\033[44m",
        "magenta": "\033[45m",
        "cyan":    "\033[46m",
        "white":   "\033[47m"
    }

    styles = {
        "bold":       "\033[1m",
        "dim":        "\033[2m",
        "italic":     "\033[3m",
        "underline":  "\033[4m",
        "blink":      "\033[5m",
        "reverse":    "\033[7m",
        "strikethrough": "\033[9m",
        "reset":      "\033[0m"
    }

    
    print(f"{styles['bold']}{colors[color]}",end='')
    print(text)
    print("\033[0m")
