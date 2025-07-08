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
bar1 = 'upn400'
bar2 = 'upn380'
bar3 = 'upn300'
bar4 = 'upn380'
bar5 = 'upn300'
bar6 = 'upn300'

# estructura2 del tp
datos = {
    # Fuerzas
    'inc': [
        # 1
        [0, False],

        # 2
        [0, False],

        # 3
        [0, False],

        # 4
        [0, False],

        # 5
        [0, False],

        # 6
        [-3750.0e3, True],

        # 7
        [0, True],

        # 8
        [0, True],

        # 9
        [0, True],

        # 10
        [0, True],

        # 11
        [0, True],

        # 12
        [0, True],

        # 13
        [-1666.66e3+3750.0e3, True],

        # 14
        [0, True],

        # 15
        [-1250e3, True],

        # 16
        [-500e3, True],

        # 17
        [0, True],

        # 18
        [0, False],

        # 19
        [0, False],

        # 20
        [0, False],

        # 21
        [1666.66e3, True],

    ]    # bar,noi,nof,are,mod,iner (m, N)
    , 'iba': [
        [1, 1, 8, 2*denom[bar1]['ag'], mod, 2*denom[bar1]['ix']],
        [2, 2, 9, 2*denom[bar2]['ag'], mod, 2*denom[bar2]['ix']],
        [3, 9, 5, 2*denom[bar3]['ag'], mod, 2*denom[bar3]['ix']],
        [4, 2, 7, 2*denom[bar4]['ag'], modt, 2*denom[bar4]['ix']],
        [5, 3, 4, 2*denom[bar5]['ag'], mod, 2*denom[bar5]['ix']],
        [6, 6, 5, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
    ],

    # designaciones
    'desig': {
        1: denom[bar1],
        2: denom[bar2],
        3: denom[bar3],
        4: denom[bar4],
        5: denom[bar5],
        6: denom[bar6],
    },


    # nod,imn,ifx,ify,cox,coy
    'ino': [
        [
            1, 3, 2, 1,
            0, 0.036],
        [
            2, 6, 5, 4,
            0.356, 0.036],
        [
            3, 9, 11, 10,
            10, 35],
        [
            4, 12, 14, 15,
            30, 20],
        [
            5, 21, 17, 16,
            50, 20],
        [
            6, 18, 20, 19,
            50, 10],
        [
            7, 18, 20, 19,
            50, 10],
        [
            8, 18, 20, 19,
            50, 10],
        [
            9, 18, 20, 19,
            50, 10],
        [
            10, 18, 20, 19,
            50, 10],
        [
            11, 18, 20, 19,
            50, 10],
        [
            12, 18, 20, 19,
            50, 10],
        [
            13, 18, 20, 19,
            50, 10],
        [
            14, 18, 20, 19,
            50, 10],
        [
            15, 18, 20, 19,
            50, 10],
        [
            16, 18, 20, 19,
            50, 10],
        [
            17, 18, 20, 19,
            50, 10],

    ],

    # Cargas (bar, (1:ver, 2:hor ,3:tri), q)
    'car': [
        [2, 1, 50e3],
        [3, 1, 50e3],
    ],

    # soporte (tipo, nodo, angulo)
    'sop': [
        [2, 2, 0],
        [3, 1, 0],
        [3, 6, 0],
    ],

    # configuraciones
    'con': [
        # xmin, xmax, ymin, ymax, escm, escq, escn
        -3, 60, -2, 40, 1/300000, 1/60000, 1/600000
    ]
}
