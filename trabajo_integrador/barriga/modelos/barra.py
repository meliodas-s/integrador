from dataclasses import dataclass
import numpy as np


class Esfuerzo:
    pass

    def graficar(self):
        pass


class Momento(Esfuerzo):
    pass


class Cortante(Esfuerzo):
    pass


class Normal(Esfuerzo):
    pass


@dataclass
class Barra:
    """
    Clase que representa una barra estructural de un sistema en 2D o 3D.

    Atributos:
    ----------
    bar : int
        Identificador único de la barra.

    noi : int
        Nodo inicial de la barra (ID del nodo).

    nof : int
        Nodo final de la barra (ID del nodo).

    are : float
        Área de la sección transversal de la barra (en unidades consistentes).

    mod : float
        Módulo de elasticidad del material (E) o módulo de Young.

    ine : float
        Momento de inercia de la barra respecto a su eje transversal.

    tra : np.array
        Matriz de transformación que relaciona coordenadas locales y globales.

    rig : np.array
        Matriz de rigidez.

    nim : int
        Índice global asociado al momento en el nodo inicial.

    nix : int
        Índice global asociado a la fuerza en X en el nodo inicial.

    niy : int
        Índice global asociado a la fuerza en Y en el nodo inicial.

    nfm : int
        Índice global del momento en el nodo final.

    nfx : int
        Índice global de la fuerza en X en el nodo final.

    nfy : int
        Índice global de la fuerza en Y en el nodo final.
    """
    bar: int
    noi: int
    nof: int
    are: float
    mod: float
    ine: float
    
    # ids de esfuerzos en nodo cercano
    nim: int
    nix: int
    niy: int
    
    # ids de esfuerzos en nodo lejanos
    nfm: int
    nfx: int
    nfy: int
    
    # coordenadas
    xin: float
    xfi: float
    yin: float
    yfi: float
    
    # matrices y ecuaciones
    tra: np.array = None
    rig: np.array = None
    mom: Momento = None
    cor: Cortante = None
    nor: Normal = None

    def cal_lmx(self):
        self.lmx = (self.xfi-self.xin)/self.lar

    def cal_lmy(self):
        self.lmy = (self.yfi-self.yin)/self.lar

    def cal_tra(self):
        # Matris de transformacion
        self.tra = (
            np.array(
                [
                    [self.lmx, self.lmy, 0, 0, 0, 0],
                    [-self.lmy, self.lmx, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, self.lmx, self.lmy, 0],
                    [0, 0, 0, -self.lmy, self.lmx, 0],
                    [0, 0, 0, 0, 0, 1]
                ]
            )
        )

    def cal_ril(self):
        # Hay terminos repetirdos
        te1 = self.are*self.mod/self.lar
        te2 = 12*self.mod*self.ine/self.lar**3
        te3 = 6*self.mod*self.ine/self.lar**2
        te4 = 4*self.mod*self.ine/self.lar
        te5 = 2*self.mod*self.ine/self.lar

        # Matriz rigidez local de la barra (k`)
        self.ril = (
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

    def cal_rig(self):
        # Calculo la matriz de rigidez global (k) y guardo.
        self.rig = (self.tra.T@self.ril)@self.tra

    def cal_lar(self):
        self.lar = np.sqrt((self.xfi-self.xin)**2+(self.yfi-self.yin)**2)
