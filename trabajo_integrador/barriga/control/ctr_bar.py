from ..modelos.barra import Barra
import pandas as pd


class CtrB:
    dtf: pd.DataFrame
    lis: dict[int, Barra]
    """
    parameters
    ----------
        dat: lista de datos [[bar,noi,nof,are,mod,iner],...]
        lis: diccionario de objetos Barra
    """
    noc: list[str] = ['bar', 'noi', 'nof', 'are', 'mod', 'ine']

    def __init__(self, dat: list[tuple[int, int, int, float, float, float]]):
        self.dtf = pd.DataFrame(dat, columns=self.noc)
        self.dtf.set_index('bar', inplace=True)  # type: ignore
        self.lis = {}

    def cargar(self, lno, lde):
        '''Funcion encargada de cargar barras
        to-do: cambiar el indice de tener que pasarlo a entero a que
        venga como entero

        parameters
        ----------
        lno: lista de objetos Nodo
        lde: lista o diccionario de objetos Designaciones
        '''
        # merge de datos
        for idx, fil in self.dtf.iterrows():

            # nodos que conectan a esa barra
            noi = fil['noi']
            nof = fil['nof']

            # creo una nueva barra
            self.lis[idx] = Barra(
                idx,
                fil['are'],
                fil['mod'],
                fil['ine'],
                lno[int(noi)],
                lno[int(nof)],
                desig=lde[idx],
            )
            self.lis[idx].cal_lar()
            self.lis[idx].cal_lmx()
            self.lis[idx].cal_lmy()
            self.lis[idx].cal_tra()
            self.lis[idx].cal_ril()
            self.lis[idx].cal_rig()
            self.lis[idx].cal_ang()

    def cal(self):
        """Funcion encargada de calculoar los valores        
        """
        for i in self.lis.values():
            i.cal_mom()
            i.cal_cor()
            i.cal_nor()

