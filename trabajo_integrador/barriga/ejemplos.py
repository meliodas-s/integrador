ejemplo1 = {
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
        [-20.833e3, True],

        # 7
        [0, False],

        # 8
        [0, False],

        # 9
        [0, False],

        # 10
        [9e3, True],
    ],

    # bar,noi,nof,are,mod,iner (m, N)
    'iba': [
        [1, 1, 4, 0.1, 2000, 0.1],
        [2, 2, 3, 0.1, 2000, 0.1],
    ],

    # nod,imn,ifx,ify,cox,coy
    'ino': [
        [1, 3, 2, 1, 0, 0],
        [2, 6, 5, 4, 0, 3],
        [3, 9, 8, 7, 5, 3],

        # nodos extra para pasadores
        [4, 10, 5, 4, 0, 3],
    ],

    # Cargas (bar, (1:ver, 2:hor ,3:tri), q)
    'car': [
        [1, 3, 30e3],
        [2, 1, 10e3]
    ],

    # soporte (tipo, nodo, angulo)
    'sop': [
        [1, ]
    ]
}

# estructura2 del tp
ejemplo2 = {
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
        [1, 1, 7, 0.1, 2000, 0.1],
        [2, 3, 2, 0.1, 2000, 0.1],
        [3, 2, 4, 0.1, 2000, 0.1],
        [4, 4, 5, 0.1, 2000, 0.1],
        [5, 6, 5, 0.1, 2000, 0.1],
    ],

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
        -3, 25, -2, 10, 1/15000, 1/5000, 1/5000
    ]
}

# estructura1 del tp
ejemplo3 = {
    # Fuerzas
    'inc': [
        # 1
        [0, False],

        # 2
        [0, False],

        # 3
        [0, False],

        # 4
        [-25e3, False],

        # 5
        [13.5e3, False],

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
        [-50e3, True],

        # 14
        [0, True],

        # 15
        [83.333e3, True],

        # 16
        [0, True],

        # 17
        [0, True],

        # 18
        [0, True],

        # 19
        [-20.83e3, False],

        # 20
        [0, False],

        # 21
        [0, False],

        # 22
        [0, True],
        
        # 23
        [0, True],



    ]    # bar,noi,nof,are,mod,iner (m, N)
    , 'iba': [
        [1, 1, 9, 0.1, 2000, 0.1],
        [2, 7, 11, 0.1, 2000, 0.1],
        [3, 4, 5, 0.1, 2000, 0.1],
        [4, 2, 8, 0.1, 2000, 0.1],
        [5, 3, 10, 0.1, 2000, 0.1],
        [6, 5, 6, 0.1, 2000, 0.1],
    ],

    # nod,imn,ifx,ify,cox,coy
    'ino': [
        [1, 3, 2, 1, 10, 0],
        [2, 6, 5, 4, 0, 20],
        [3, 12, 9, 8, 10, 35],
        [4, 23, 14, 13, 30, 20],
        [5, 18, 17, 16, 50, 20],
        [6, 21, 20, 19, 50, 10],

        # nodos extra por barra para pasadores
        [7, 7, 5, 4, 0, 20],
        [8, 10, 9, 8, 10, 35],
        [9, 11, 9, 8, 10, 35],
        [10, 15, 14, 13, 30, 20],
        [11,22, 14, 13, 30, 20]
    ] 
    , 
    # Cargas (bar, (1:ver, 2:hor ,3:tri), q)
    'car': [
        [2, 3, 30e3],
        [3, 1, 10e3],
    ],

    # soporte (tipo, nodo, angulo)
    'sop': [
        [2, 1, 0],
        [3, 3, 0],
        [3, 6, 0],
    ],

    # configuraciones
    'con': [
        # xmin, xmax, ymin, ymax, escm, escq, escn
        -1, 60, -2, 40, 1/15000, 1/5000, 1/5000
    ]
}
