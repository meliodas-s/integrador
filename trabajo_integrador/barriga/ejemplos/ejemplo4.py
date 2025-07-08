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
bar6 = 'upn80'
bar7 = 'upn80'
bar8 = 'upn80'
bar9 = 'upn80'
bar10 = 'upn80'
bar11 = 'upn80'
bar12 = 'upn80'
bar13 = 'upn80'
bar14 = 'upn80'
bar15 = 'upn80'
bar16 = 'upn80'
bar17 = 'upn80'
bar18 = 'upn80'
bar19 = 'upn80'
bar20 = 'upn80'
bar21 = 'upn80'
bar22 = 'upn80'
bar23 = 'upn80'
bar24 = 'upn80'
bar25 = 'upn80'
bar26 = 'upn80'
bar27 = 'upn80'
bar28 = 'upn80'
bar29 = 'upn80'
bar30 = 'upn80'
bar31 = 'upn80'
bar32 = 'upn80'
bar33 = 'upn80'

# estructura2 del tp
datos = {
    # Fuerzas
    'inc': [
        # 1
        [0, True],

        # 2
        [0, True],

        # 3
        [0, True],

        # 4
        [0, True],

        # 5
        [0, True],

        # 6
        [0, True],

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
        [0, False],

        # 14
        [0, False],

        # 15
        [0, True],

        # 16
        [0, True],

        # 17
        [0, True],

        # 18
        [0, True],

        # 19
        [0, True],

        # 20
        [0, True],

        # 21
        [0, True],

        # 22
        [0, False],

        # 23
        [0, False],

        # 24
        [0, True],

        # 25
        [0, True],

        # 26
        [0, True],

        # 27
        [0, True],

        # 28
        [0, True],

        # 29
        [0, True],

        # 30
        [0, True],

        # 31
        [0, True],

        # 32
        [0, True],

        # 33
        [0, True],

        # 34
        [0, True],

        # 35
        [0, True],

        # 36
        [0, True],

        # 37
        [0, True],

        # 38
        [0, True],

        # 39
        [0, True],

        # 40
        [0, True],

        # 41
        [0, True],

        # 42
        [0, True],

        # 43
        [0, False],

        # 44
        [0, False],

        # 45
        [0, True],

        # 46
        [0, True],

        # 47
        [0, True],

        # 48
        [0, True],

        # 49
        [0, False],

        # 50
        [0, False],

        # 51
        [0, True],


    ]    # bar,noi,nof,are,mod,iner (m, N)
    , 'iba': [
        [1, 1, 2, 2*denom[bar1]['ag'], mod, 2*denom[bar1]['ix']],
        [2, 2, 3, 2*denom[bar2]['ag'], mod, 2*denom[bar2]['ix']],
        [3, 3, 4, 2*denom[bar3]['ag'], mod, 2*denom[bar3]['ix']],
        [4, 4, 5, 2*denom[bar4]['ag'], modt, 2*denom[bar4]['ix']],
        [5, 5, 6, 2*denom[bar5]['ag'], mod, 2*denom[bar5]['ix']],
        [6, 1, 7, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [7, 1, 8, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [8, 2, 8, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [9, 2, 9, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [10, 3, 9, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [11, 9, 4, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [12, 4, 10, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [13, 4, 11, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [14, 5, 11, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [15, 6, 12, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [16, 7, 8, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [17, 8, 9, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [18, 9, 10, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [19, 10, 11, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [20, 11, 12, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [21, 7, 13, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [22, 8, 13, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [23, 13, 9, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [24, 14, 9, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [25, 9, 15, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [26, 15, 10, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [27, 10, 16, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [28, 16, 11, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [29, 13, 14, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [30, 14, 15, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [31, 15, 16, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [32, 16, 17, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
        [33, 17, 11, 2*denom[bar5]['ag'], modt, 2*denom[bar5]['ix']],
    ],

    # designaciones
    'desig': {
        1: denom[bar1],
        2: denom[bar2],
        3: denom[bar3],
        4: denom[bar4],
        5: denom[bar5],
        6: denom[bar6],
        7: denom[bar7],
        8: denom[bar8],
        9: denom[bar9],
        10: denom[bar10],
        11: denom[bar11],
        12: denom[bar12],
        13: denom[bar13],
        14: denom[bar14],
        15: denom[bar15],
        16: denom[bar16],
        17: denom[bar17],
        18: denom[bar18],
        19: denom[bar19],
        20: denom[bar20],
        21: denom[bar21],
        22: denom[bar22],
        23: denom[bar23],
        24: denom[bar24],
        25: denom[bar25],
        26: denom[bar26],
        27: denom[bar27],
        28: denom[bar28],
        29: denom[bar29],
        30: denom[bar30],
        31: denom[bar31],
        32: denom[bar32],
        33: denom[bar33],
    },


    # nod, imn, ifX, ifY, cox, coy
    'ino': [
        [
            1, 3, 2, 1,
            0.000, 0.036],
        [
            2, 15, 14, 13,
            0.350, 0.036],
        [
            3, 24, 23, 22,
            0.724, 0.036],
        [
            4, 30, 29, 28,
            1.291, 0.000],
        [
            5, 45, 44, 43,
            2.010, 0.000],
        [
            6, 51, 50, 49,
            2.315, 0.036],
        [
            7, 6, 5, 4,
            0.000, 0.356],
        [
            8, 12, 11, 10,
            0.350, 0.227],
        [
            9, 21, 20, 19,
            0.697, 0.227],
        [
            10, 33, 32, 31,
            1.325, 0.227],
        [
            11, 42, 41, 40,
            2.010, 0.227],
        [
            12, 48, 47, 46,
            2.315, 0.227],
        [
            13, 9, 8, 7,
            0.350, 0.476],
        [
            14, 18, 17, 16,
            0.650, 0.557],
        [
            15, 27, 26, 25,
            0.993, 0.391],
        [
            16, 36, 35, 34,
            1.395, 0.614],
        [
            17, 39, 38, 37,
            1.395, 1.137],

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
