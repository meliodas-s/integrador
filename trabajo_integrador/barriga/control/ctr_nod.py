from ..modelos.nodo import Nodo
import pandas as pd


# controlador de nodos
class CtrN:
    """
    parameters
    ----------
        ino: lista de nodos [[ide, idm, idx, idy, cox, coy],...]
    nos: lista de nodos

    """
    noc = ['nod', 'imn', 'ifx', 'ify', 'cox', 'coy']

    def __init__(self, ino: list[tuple[int, int, int, int, float, float]]):
        self.lno: list[Nodo] | None = None
        self.dtf = pd.DataFrame(ino, columns=self.noc)
        self.dtf.set_index('nod', inplace=True)

    def cargar(self):
        pass
