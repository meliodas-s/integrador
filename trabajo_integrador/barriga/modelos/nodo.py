class Nodo:
    '''
    ide, identificador 
    idm, id del momento
    idx, id de la fuerza en coordenadas globales en x
    idy, id de la fuerza en coordenadas globales en y
    cox, coordenada en x del nodo
    coy, coordenada en y del nodo
    '''

    def __init__(
        self,
        ide: int,
        idm: int,
        idx: int,
        idy: int,
        cox: float,
        coy: float
    ):
        self.ide = ide
        self.idm = idm
        self.idx = idx
        self.idy = idy
        self.cox = cox
        self.coy = coy
