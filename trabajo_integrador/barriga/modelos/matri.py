import pandas as pd
import numpy as np

class SolvIt:
    """ Clase encargada de resolver el sistema.
    
    Parameters
    ----------
    inc: incognitas de fuerza y desplazamientos [[float,bool],...]
    """
    def __init__(self, incog):
        ncc = ['fue', 'des']
        self.inc = pd.DataFrame(incog, columns=ncc)
        
        # cantidad de libertades
        self.cal = self.inc.shape[0]
        
        # Numeracion del 1 al n(numero de libertades)
        nli = np.arange(1, self.cal+1)

        # Crear data-frame de rigidez
        self.rig = pd.DataFrame(0, index=nli, columns=nli).astype(float)
    pass