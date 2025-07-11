from ..modelos.nodo import Nodo
import pandas as pd


# controlador de nodos
class CtrN:
    dtf: pd.DataFrame
    lno: dict[int, Nodo]
    """
    parameters
    ----------
        ino: lista de nodos [[ide, idm, idx, idy, cox, coy],...]
    nos: lista de nodos

    """
    noc:list[str] = ['nod', 'imn', 'ifx', 'ify', 'cox', 'coy']

    def __init__(self, ino: list[tuple[int, int, int, int, float, float]]):
        self.dtf = pd.DataFrame(ino, columns=self.noc)
        self.dtf.set_index('nod', inplace=True) # type: ignore


    def cargar(self):
        # for _, fila in self.dtf.iterrows():
        #     self.dtf[1] = Nodo(
        #         fila['nod'],
        #         fila['imn'],
        #         fila['ifx'],
        #         fila['ify'],
        #         fila['cox'],
        #         fila['coy']
        #     )
        pass