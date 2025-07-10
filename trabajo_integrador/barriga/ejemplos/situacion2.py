# modulo de elasticidad en N/m2
mod = 21e3*(1e6)
modt = 210e3*(1e6)
import math

# perfiles (todos los datos en m)
denom = {
    "38.1mm x 1.6mm": {
        "nombre": "38.1mm x 1.6mm",
        "ag": 1.835*10**(-4),
        "ix": 3.061*10**(-8),

        # para completar
        'sx': 3.061*10**(-8)/(38.1e3/2),
        'ra': 38.1e-3/2,
        'tf':1.6e-3,

        # sx = 8π​(R4−r4) (para media seccion)
        'qx': 8*math.pi*((38.1e-3/2)**4-(38.1e-3/2-1.6e-3)**4)
    },

    "38.1mm x 2mm": {
        "nombre": "38.1mm x 2mm",
        "ag": 2.268*10**(-4),
        "ix": 3.706*10**(-8),

        # para completar
        'sx': 3.706*10**(-8)/(38.1e-3/2),
        'ra': 38.1e-3/2,
        'tf':2e-3,
        'qx': 8*math.pi*((38.1e-3/2)**4-(38.1e-3/2-2e-3)**4)
    },

    "38.1mm x 2.5mm": {
        "nombre": "38.1mm x 2.5mm",
        "ag": 2.796*10**(-4),
        "ix": 4.451*10**(-8),

        # para completar
        'sx': 4.451*10**(-8)/(38.1e-3/2),
        'ra': 38.1e-3/2,
        'tf':2e-3,
        'qx': 8*math.pi*((38.1e-3/2)**4-(38.1e-3/2-2.5e-3)**4)
    },
    
    "41.25mm x 2.5mm": {
        "nombre": "41.25mm x 2.5mm",
        "ag": 3.045*10**(-4),
        "ix": 5.852*10**(-8),

        # para completar
        'sx': 5.852*10**(-8)/(41.25e-3/2),
        'ra': 41.25e-3/2,
        'tf':2.5e-3,
        'qx':8*math.pi*((41.25e-3/2)**4-(41.25e-3/2-2.5e-3)**4)
    },
    
    "44.44mm x 2mm": {
        "nombre": "44.44mm x 2mm",
        "ag": 2.667*10**(-4),
        "ix": 6.129*10**(-8),

        # para completar
        'sx': 6.129*10**(-8)/(44.44e-3/2),
        'ra': 44.44e-3/2,
        'tf':2e-3,
        'qx':8*math.pi*((44.44e-3/2)**4-(44.44e-3/2-2e-3)**4)
    },
    
    "76.20x2": {
        "nombre": "76.2mm x 2mm",
        "ag": 4.662*10**(-4),
        "ix": 32.705*10**(-8),

        # para completar
        'sx': 32.705*10**(-8)/(76.2e-3/2),
        'ra': 76.2e-3/2,
        'tf':2e-3,
        'qx':8*math.pi*((76.2e-3/2)**4-(76.2e-3/2-2e-3)**4)
    },
    
    "139.70x6.35": {
        "nombre": "139.70mm x 6.35mm",
        "ag": 26.602*10**(-4),
        "ix": 603.66*10**(-8),

        # para completar
        'sx': 603.66*10**(-8)/(76.2e-3/2),
        'ra': 139.70e-3/2,
        'tf': 6.35e-3,
        'qx':8*math.pi*((139.70e-3/2)**4-(139.70e-3/2-6.35e-3)**4)
    }
}

# eleccion que elegi
bar1 = '139.70x6.35'
bar2 = '139.70x6.35'
bar3 = '139.70x6.35'
bar4 = '139.70x6.35'
bar5 = '139.70x6.35'
bar6 = '139.70x6.35'
bar7 = '139.70x6.35'
bar8 = '139.70x6.35'
bar9 = '139.70x6.35'
bar10 = '139.70x6.35'
bar11 = '139.70x6.35'
bar12 = '139.70x6.35'
bar13 = '139.70x6.35'
bar14 = '139.70x6.35'
bar15 = '139.70x6.35'
bar16 = '139.70x6.35'
bar17 = '76.20x2'
bar18 = '76.20x2'
bar19 = '76.20x2'
bar20 = '76.20x2'
bar21 = '76.20x2'
bar22 = '76.20x2'
bar23 = '76.20x2'
bar24 = '139.70x6.35'
bar25 = '139.70x6.35'
bar26 = '139.70x6.35'
bar27 = '139.70x6.35'
bar28 = '139.70x6.35'
bar29 = '139.70x6.35'
bar30 = '139.70x6.35'
bar31 = '139.70x6.35'
bar32 = '139.70x6.35'
bar33 = '139.70x6.35'

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
        [0, True],

        # 14
        [0, True],

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
        [0, False],

        # 29
        [0, False],

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
        [-5e3, True],

        # 38
        [6e4, True],

        # 39
        [0, True],

        # 40
        [0, True],

        # 41
        [0, True],

        # 42
        [0, True],

        # 43
        [0, True],

        # 44
        [0, True],

        # 45
        [0, True],

        # 46
        [0, True],

        # 47
        [0, True],

        # 48
        [0, True],

        # 49
        [0, True],

        # 50
        [0, True],

        # 51
        [0, True],


    ]    # bar,noi,nof,are,mod,iner (m, N)
    , 'iba': [
        [1, 1, 2, denom[bar1]['ag'], mod, denom[bar1]['ix']],
        [2, 2, 3, denom[bar2]['ag'], modt, denom[bar2]['ix']],
        [3, 3, 4, denom[bar3]['ag'], mod, denom[bar3]['ix']],
        [4, 4, 5, denom[bar4]['ag'], modt, denom[bar4]['ix']],
        [5, 5, 6, denom[bar5]['ag'], modt, denom[bar5]['ix']],
        [6, 1, 7, denom[bar6]['ag'], modt, denom[bar6]['ix']],
        [7, 1, 8, denom[bar7]['ag'], modt, denom[bar7]['ix']],
        [8, 2, 8, denom[bar8]['ag'], modt, denom[bar8]['ix']],
        [9, 2, 9, denom[bar9]['ag'], mod, denom[bar9]['ix']],
        [10, 3, 9, denom[bar10]['ag'], mod, denom[bar10]['ix']],
        [11, 9, 4, denom[bar11]['ag'], modt, denom[bar11]['ix']],
        [12, 4, 10, denom[bar12]['ag'], modt, denom[bar12]['ix']],
        [13, 4, 11, denom[bar13]['ag'], modt, denom[bar13]['ix']],
        [14, 5, 11, denom[bar14]['ag'], mod, denom[bar14]['ix']],
        [15, 6, 12, denom[bar15]['ag'], mod, denom[bar15]['ix']],
        [16, 7, 8, denom[bar16]['ag'], mod, denom[bar16]['ix']],
        [17, 8, 9, denom[bar17]['ag'], mod, denom[bar17]['ix']],
        [18, 9, 10, denom[bar18]['ag'], mod, denom[bar18]['ix']],
        [19, 10, 11, denom[bar19]['ag'], modt, denom[bar19]['ix']],
        [20, 11, 12, denom[bar20]['ag'], modt, denom[bar20]['ix']],
        [21, 7, 13, denom[bar21]['ag'], modt, denom[bar21]['ix']],
        [22, 8, 13, denom[bar22]['ag'], mod, denom[bar22]['ix']],
        [23, 13, 9, denom[bar23]['ag'], modt, denom[bar23]['ix']],
        [24, 14, 9, denom[bar24]['ag'], mod, denom[bar24]['ix']],
        [25, 9, 15, denom[bar25]['ag'], mod, denom[bar25]['ix']],
        [26, 15, 10, denom[bar26]['ag'], modt, denom[bar26]['ix']],
        [27, 10, 16, denom[bar27]['ag'], modt, denom[bar27]['ix']],
        [28, 16, 11, denom[bar28]['ag'], mod, denom[bar28]['ix']],
        [29, 13, 14, denom[bar29]['ag'], modt, denom[bar29]['ix']],
        [30, 14, 15, denom[bar30]['ag'], modt, denom[bar30]['ix']],
        [31, 15, 16, denom[bar31]['ag'], mod, denom[bar31]['ix']],
        [32, 16, 17, denom[bar32]['ag'], mod, denom[bar32]['ix']],
        [33, 17, 11, denom[bar33]['ag'], mod, denom[bar33]['ix']],
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
            1.33, 0.227],
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
            0.992, 0.391],
        [
            16, 36, 35, 34,
            1.395, 0.614],
        [
            17, 39, 38, 37,
            1.395, 1.137],

    ],

    # Cargas (bar, (1:ver, 2:hor ,3:tri), q:en positivo)
    'car': [],

    # soporte (tipo, nodo, angulo)
    'sop': [
        [2,3,  0],
        [2,4,  0],
    ],

    # configuraciones
    'con': [
        # xmin, xmax, ymin, ymax, escm, escq, escn
        -1, 3, -1, 2, 1/6000, 1/30000, 1/60000
    ],

    # pesos en kg
    'pesos': {
        1: 0.77,
        2: 0.67,
        3: 0.82,
        4: 1.04,
        5: 0.44,
        6: 0.70,
        7: 0.88,
        8: 0.34,
        9: 0.71,
        10: 0.28,
        11: 0.92,
        12: 0.33,
        13: 1.09,
        14: 0.33,
        15: 0.28,
        16: 0.54,
        17: 0.50,
        18: 0.91,
        19: 0.98,
        20: 0.44,
        21: 0.53,
        22: 0.36,
        23: 0.62,
        24: 0.48,
        25: 0.49,
        26: 0.54,
        27: 0.57,
        28: 1.05,
        29: 0.45,
        30: 0.55,
        31: 0.66,
        32: 0.75,
        33: 1.58,
    }
}
