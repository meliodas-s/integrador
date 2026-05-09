import pandas as pd
import numpy as np
from ..modelos.barra import Barra
from ..modelos.carga import Carga
import sympy as sp


class SolvIt:
    """ Clase encargada de resolver el sistema.

    Parameters
    ----------
    inc: incognitas de fuerza y desplazamientos [[float,bool],...]
    sit: situacion que se plantea (Cargas vertical o horizontal)
    car: cargas en listas [[int,int...]...]
    """

    def __init__(self, incog, sit, car):
        ncc = ['fue', 'des']
        self.inc = pd.DataFrame(incog, columns=ncc)

        # situacion
        self.sit = sit

        # cantidad de libertades
        self.cal = self.inc.shape[0]

        # Numeracion del 1 al n(numero de libertades)
        nli = np.arange(1, self.cal+1)

        # Crear data-frame de rigidez
        self.rig = pd.DataFrame(0, index=nli, columns=nli).astype(float)
        
        # cargas en formato lista
        self.car = car

        # Lista de cargas
        self.cgs: list[Carga] = []

    def car_car(self):
        # Controlador de cargas (si la situacion es 'n')
        # Si la situacion es n, car es una lista vacia.
        # (no va aqui)
        # si la situacion es otra tambien se ejecuta.
        for i in self.car:
            print(i)
            self.cgs.append(Carga(i[0], i[1], i[2]))

    def car_des(self, cag: float, sit: str, lba: dict[int, Barra], pes):
        '''funcion encargada de cargar nodos
        dependiendo si es una situacion de carga verticales
        o cargas horizonales. Ejemplo: un choque o el peso
        mismo de la estructura (1g, 2g, etc)

        - Por convencion el signo de la carga vertical
        ira positivo si es que la carga va de arriba a abajo

        Parameter
        ---------
        cag: cantidad de fuerzas g
        sit: situacion a usar ['v','h','n']
        lba: diccionario de barras
        pes: lista con pesos de la barra
        '''
        grav = 9.8

        match sit:

            # gravedad Nm/s2
            case 'h':
                for bar in lba.values():
                    bar.mas = pes[bar.bar]

                    # creo carga vertical [N/m2]
                    cargv = grav*cag*bar.mas/bar.lar

                    # componentes en x e y
                    cargvx = cargv*np.cos(bar.ang)
                    cargvy = cargv*np.sin(bar.ang)
                    print(cargv)


                    # fuerzas horizontales en ambos nodods
                    qh = cargv*bar.lar/2

                    # momento en a (nodo incia)
                    moi = -cargvy*bar.lar**2/12

                    # momento en a (nodo final)
                    mof = cargvy*bar.lar**2/12

                    # se suman los datos a las incognitas
                    self.inc.at[bar.noi.idm-1, 'fue'] += round(moi, 5)
                    self.inc.at[bar.nof.idm-1, 'fue'] += round(mof, 5)
                    self.inc.at[bar.noi.idx-1, 'fue'] += qh
                    self.inc.at[bar.nof.idx-1, 'fue'] += qh
                    print(self.inc)

                    # se guardan las cargas
                    self.car.append([bar.bar, 1, round(cargvy, 5)])
                    self.car.append([bar.bar, 2, round(cargvx, 5)])

            case 'v':
                for bar in lba.values():
                    bar.mas = pes[bar.bar]

                    # creo carga vertical [N/m2]
                    cargv = grav*cag*bar.mas/bar.lar

                    # componentes en x e y
                    cargvx = -cargv*np.sin(bar.ang)
                    cargvy = cargv*np.cos(bar.ang)

                    # fuerzas verticales en ambos nodods
                    qv = cargv*bar.lar/2

                    # momento en a (nodo incia)
                    moi = -cargvy*bar.lar**2/12

                    # momento en a (nodo final)
                    mof = cargvy*bar.lar**2/12

                    # se suman los datos a las incognitas
                    self.inc.at[bar.noi.idm-1, 'fue'] += round(moi, 5)
                    self.inc.at[bar.nof.idm-1, 'fue'] += round(mof, 5)
                    self.inc.at[bar.noi.idy-1, 'fue'] += -qv
                    self.inc.at[bar.nof.idy-1, 'fue'] += -qv

                    # se guardan las cargas
                    self.car.append([bar.bar, 1, round(cargvy, 5)])
                    self.car.append([bar.bar, 2, round(cargvx, 5)])

            case 'n':
                pass

    def mrb(self, bar: Barra, rig: pd.DataFrame):
        '''Carga la matriz de rigiddez para cada barra.
        Dada la barra y la matriz de rigidez suma sus respectivo
        aporte en cada pocision.
        '''
        # filas(indices) de momentos, fuerx, fuery
        fid = [
            bar.noi.idx,
            bar.noi.idy,
            bar.noi.idm,
            bar.nof.idx,
            bar.nof.idy,
            bar.nof.idm,
        ]

        # columnas(indices)
        cid = fid

        # Convierto (k) en df para coincidencia de indices.
        mrg = pd.DataFrame(bar.rig, index=fid, columns=cid)

        # guarda la matriz indexda
        bar.rgi = mrg

        # Sumar los valores nuevos a la submatriz original
        sum = rig.loc[fid, cid].values + mrg
        rig.loc[fid, cid] = pd.DataFrame(sum, index=fid, columns=cid)

    def carga(self, lba: dict[int, Barra]):
        """Crea la matriz de rigidez global

        Parameters
        ---------
        lba: lista de objetos Barras
        """
        # se suma todo en la matriz de rigidez
        for bar in lba.values():
            self.mrb(bar, self.rig)

    def creas(self):
        """Funcion encargada de crear matrices simbolicas
        """
        # se crea matriz symbolica rigSimbolica
        self.rgs = sp.Matrix(self.rig.values)

        # defino matrizes de Desplaza e Incog.(fuerzas)
        self.mde = sp.Matrix()
        self.min = sp.Matrix()

        # defino incog. simbolicas de Desplaza y Fuerzas
        self.isd = sp.Matrix()
        self.isf = sp.Matrix()

        # incognitas totales
        self.igt = []

    def cargi(self):
        """Funcion encargada de cargar incognias
        fuerzas y desplazamientos
        """

        # 🔹 Controlador de ecuaciones
        # se crean los datos de las incognitas
        for idx, fil in self.inc.iterrows():
            if not fil['des']:
                fue = sp.symbols(f'Q_{idx + 1}')
                self.mde = self.mde.col_join(sp.Matrix([0]))
                self.min = self.min.col_join(sp.Matrix([fue]))

                # Agrego la incognita fuerza
                self.isd = self.isd.col_join(sp.Matrix([0]))
                self.isf = self.isf.col_join(sp.Matrix([fue]))
                self.igt.append(fue)

            else:
                des = sp.symbols(f'D_{idx + 1}')
                self.mde = self.mde.col_join(sp.Matrix([des]))
                self.min = self.min.col_join(sp.Matrix([fil['fue']]))

                # Agrego la incognita despla
                self.isd = self.isd.col_join(sp.Matrix([des]))
                self.isf = self.isf.col_join(sp.Matrix([fil['fue']]))
                self.igt.append(des)

    def solvi(self):
        """Funcion encargada de resolver el sistema usando
        la mtriz de rigidez. Ademas guarda los valores resultado
        en una matriz sympy (ecu)
        """
        # matriz resultante de incognitas
        self.res = self.rgs * self.mde
        self.eqs = []

        # cargo eqs con los items de res
        for idx in range(self.res.rows):
            self.eqs.append(sp.Eq(self.min[idx], self.res[idx]))

        self.sol = sp.solve(self.eqs, self.igt)
        self.isd = self.isd.subs(self.sol)
        self.isf = self.isf.subs(self.sol)

        # guardo la ecuaciond de igualdades
        self.ecu = sp.Eq(
            sp.Matrix(list(self.sol.keys())),
            sp.Matrix(list(self.sol.values()))
        )

    def solvi_bar(self, lba):
        """Funcion que se encarga de solucionar
        de guardar las soluciones para cada barra
        """
        # consigo los valores de las fuerzas en las barras
        for bar in lba.values():

            # desplazamiento de los nodos en x e y
            den = [
                bar.noi.idx,
                bar.noi.idy,
                bar.noi.idm,
                bar.nof.idx,
                bar.nof.idy,
                bar.nof.idm,]

            # vector de desplazamientos [DNx, DNy, DFx, DFy]
            vde = np.array(
                [
                    self.isd[bar.noi.idx-1],
                    self.isd[bar.noi.idy-1],
                    self.isd[bar.noi.idm-1],
                    self.isd[bar.nof.idx-1],
                    self.isd[bar.nof.idy-1],
                    self.isd[bar.nof.idm-1],
                ]
            )

            # cálculo del esfuerzo de la barra
            esf = (bar.ril@bar.tra)@vde
            esf = pd.DataFrame(esf, index=den, columns=[f'{bar.bar}'])

            # guardo los valores
            bar.esf = esf

    def carga_bar(self, lba):
        """funcion encargada de cargar las cargas 
        en barras que las tienen. Pero esto es para 
        su graficacion por lo que deberia ir separado
        de esta clase.
        """
        # momentos en barras con cargas
        for cag in self.cgs:

            # indice de barra
            iba = cag.bar

            # barra en cuestion
            bar = lba[iba]

            match cag.tip:
                case 1:
                    bar.cav = cag
                case 2:
                    bar.cah = cag
                case 3:
                    bar.cat = cag
