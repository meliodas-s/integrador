class Denomina:
    """
    
    Parameters
    ----------
    ide: Ide de la denominacion
    nom: Nombre de la denominacion
    are: Area de la denominacion
    mix: Momento de inercia respecto al eje x
    mrs: Modulo resistente elastico (W(oller), S(iram))
    msm: Momento Estatico maximo.
    x2m: Max x2, donde hay mas momento.
    """
    def __init__(self, nom:str, are:float, mix:float, m2m:float):
        self.nom = nom
        self.are = are
        self.mix = mix
        self.m2m = m2m
        self.mrs = 0
        self.msm = 0

