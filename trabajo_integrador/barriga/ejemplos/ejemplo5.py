# modulo de elasticidad en N/m2
mod = 21e3*(1e6)
modt = 210e3*(1e6)
"""
float: Módulo de elasticidad en N/m2.
"""

# perfiles (todos los datos en m)
denom = {
    'upn80': {
        'nombre': 'upn80',
        'tf': 8e-3,
        'ag': 11e-4,
        'ix': 106e-8,
        'sx': 26.5e-5,
        'qx': 15.9e-6
    },
    'upn100': {
        'nombre': 'upn100',
        'tf': 8.5e-3,
        'ag': 13.5e-4,
        'ix': 206e-8,
        'sx': 41.2e-5,
        'qx': 24.5e-6
    },
    'upn160': {
        'nombre': 'upn160',
        'tf': 10.5e-3,
        'ag': 24e-4,
        'ix': 925e-8,
        'sx': 116e-5,
        'qx': 68.8e-6
    },
    'upn180': {
        'nombre': 'upn180',
        'tf': 11e-3,
        'ag': 28e-4,
        'ix': 1350e-8,
        'sx': 150e-5,
        'qx': 89.6e-6
    },
    'upn240': {
        'nombre': 'upn240',
        'tf': 13e-3,
        'ag': 42.3e-4,
        'ix': 3600e-8,
        'sx': 150e-5,
        'qx': 89.6e-6
    },
    'upn300': {
        'nombre': 'upn300',
        'tf': 16e-3,
        'ag': 58.8e-4,
        'ix': 8030e-8,
        'sx': 535e-5,
        'qx': 316e-6
    },
    'upn380': {
        'nombre': 'upn300',
        'tf': 16e-3,
        'ag': 80.40e-4,
        'ix': 17760e-8,
        'sx': 829e-5,
        'qx': 507e-6
    },
    'upn400': {
        'nombre': 'upn400',
        'tf': 18e-3,
        'ag': 91.5e-4,
        'ix': 20350e-8,
        'sx': 1020e-5,
        'qx': 618e-6
    },

}
"""
dict of {str: dict}: Catálogo de propiedades geométricas de perfiles UPN.
Todos los valores numéricos están expresados en metros.

Claves del sub-diccionario:
- nombre (str): Designación comercial del perfil.
- tf (float): Espesor del ala (flange thickness).
- ag (float): Área bruta de la sección transversal (gross area).
- ix (float): Momento de inercia respecto al eje X fuerte.
- sx (float): Módulo resistente elástico respecto al eje X.
- qx (float): Momento estático de la sección (primer momento de área).
"""

# eleccion de perfiles
bar1 = 'upn80'
"""
str: Designación del perfil seleccionado para las barras de la estructura.
"""

# estructura2 del tp
datos = {
    # Fuerzas
    'inc': [
        # 1
        [0, False],

        # 2
        [0, False],

        # 3
        [0, True],

        # 4
        [0, False],

        # 5
        [0, False],

        # 6
        [0, True],

    ]    # bar,noi,nof,are,mod,iner (m, N)
    , 'iba': [
        [1, 1, 2, denom[bar1]['ag'], mod, denom[bar1]['ix']],
    ],

    # designaciones
    'desig': {
        1: denom[bar1],
    },

    # nod,imn,ifx,ify,cox,coy
    'ino': [
        [1, 3, 2, 1, 0, 0],
        [2, 6, 5, 4, 5, 3],
    ],

    # Cargas (bar, (1:ver, 2:hor ,3:tri), q)
    'car': [],

    # soporte (tipo, nodo, angulo)
    'sop': [
        [2, 1, 0],
        [2, 2, 0],
    ],

    # configuraciones
    'con': [
        # xmin, xmax, ymin, ymax, escm, escq, escn
        -3, 6, -2, 5, 1/100, 1/150, 1/150
    ],
    'pesos': {
        1: 15.82,
    }
}

"""
dict: Diccionario central con toda la información geométrica, mecánica y de cargas 
para ensamblar la matriz del pórtico/estructura.

Claves del diccionario
----------------------
inc : list of list
    Vector de fuerzas nodales e incógnitas. Cada elemento sigue el formato.
    Si es_incognita_activa es True, me calcula el desplazamiento en el lugar.
    Si es_incognita_activa es False, me calculara la fuerza en esa restriccion.
    [valor_fuerza, es_incognita_activa (bool)].
iba : list of list
    Matriz de incidencias y propiedades de las barras. Formato: 
    [id_barra, nodo_inicial, nodo_final, area, modulo_elasticidad, inercia].
desig : dict of {int: dict}
    Mapeo entre el ID de la barra y el diccionario completo de sus propiedades geométricas.
ino : list of list
    Coordenadas e identificadores de grados de libertad nodales. 
    Es una vinculacion entre los datos de inc y los nodos.
    Le decimos que incognita le pertenece a cada nodo.
    Formato:
    [id_nodo, id_incognita_momento, id_incognita_fx, id_incognita_fy, coord_x, coord_y].
car : list of list
    Cargas externas aplicadas directamente sobre las barras. Formato:
    [id_barra, tipo_carga, magnitud_q], donde tipo_carga es 1: vertical, 2: horizontal, 3: triangular.
sop : list of list
    Configuración de los vínculos externos (soportes). Formato:
    [tipo_vinculo, id_nodo, angulo_rotacion].
con : list
    Configuraciones gráficas y de visualización. Formato:
    [xmin, xmax, ymin, ymax, escala_momentos, escala_cortes, escala_normales].
pesos : dict of {int: float}
    Mapeo entre el ID de la barra y su peso propio asignado.
"""