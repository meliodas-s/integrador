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
        self.lno = {}


    def cargar(self):
        '''
        Funcion encargada de crear los objetos nodo
        '''
        for ide, fila in self.dtf.iterrows():
            self.lno[ide] = Nodo(
                ide,
                fila['imn'],
                fila['ifx'],
                fila['ify'],
                fila['cox'],
                fila['coy']
            )
