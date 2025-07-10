# modulo de elasticidad en N/m2
mod = 21e3*(1e6)
modt = 210e3*(1e6)

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

# eleccion que elegi
bar1 = 'upn80'
bar2 = 'upn80'
bar3 = 'upn80'
bar4 = 'upn80'
bar5 = 'upn80'

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
        [-25e3, True],

        # 5
        [13.5e3, True],

        # 6
        [9e3-20.83e3, True],

        # 7
        [0, False],

        # 8
        [0, False],

        # 9
        [0, False],

        # 10
        [0, False],

        # 11
        [0, True],

        # 12
        [-62.5e3, True],

        # 13
        [-50e3, True],

        # 14
        [0, True],

        # 15
        [83.333e3, True],

        # 16
        [0, False],

        # 17
        [0, False],

        # 18
        [0, False],

        # 19
        [0, True],

    ]    # bar,noi,nof,are,mod,iner (m, N)
    , 'iba': [
        [1, 1, 7, 2*denom[bar1]['ag'], mod, 2*denom[bar1]['ix']],
        [2, 3, 2, 2*denom[bar2]['ag'], modt, 2*denom[bar2]['ix']],
        [3, 2, 4, 2*denom[bar3]['ag'], mod, 2*denom[bar3]['ix']],
        [4, 4, 5, 2*denom[bar4]['ag'], mod, 2*denom[bar4]['ix']],
        [5, 6, 5, 2*denom[bar5]['ag'], mod, 2*denom[bar5]['ix']],
    ],

    # designaciones
    'desig': {
        1: denom[bar1],
        2: denom[bar2],
        3: denom[bar3],
        4: denom[bar4],
        5: denom[bar5],
    },


    # nod,imn,ifx,ify,cox,coy
    'ino': [
        [1, 3, 2, 1, 0, 0],
        [2, 6, 5, 4, 5, 3],
        [3, 9, 8, 7, 5, 0],
        [4, 12, 11, 10, 10, 3],
        [5, 15, 14, 13, 20, 3],
        [6, 18, 17, 16, 20, 1],

        # nodos extra por barra para pasadores
        [7, 19, 5, 4, 5, 3],
    ]    # Cargas (bar, (1:ver, 2:hor ,3:tri), q)
    , 'car': [
        [2, 3, 30e3],
        [3, 1, 10e3],
        [4, 1, 10e3],
    ],

    # soporte (tipo, nodo, angulo)
    'sop': [
        [2, 1, 0],
        [3, 3, 0],
        [3, 6, 0],
        [1, 4, 0],
    ],

    # configuraciones
    'con': [
        # xmin, xmax, ymin, ymax, escm, escq, escn
        -3, 25, -2, 10, 1/15000, 1/15000, 1/15000
    ],
    'pesos': {
        1: 15.82,
        2: 13.71,
        3: 16.85,
        4: 21.32,
        5: 9.11
    }
}
