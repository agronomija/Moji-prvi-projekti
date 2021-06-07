import numpy as np

sudoku = np.full((9, 9), 0)


def igralna_plosca_prikaz(sudoku):
    """Funkcija za delovanje potrebuje igralno ploščo (seznam, seznamov dolžine 9 in vrne prikazan seznam seznamov."""
    for index, vrstica in enumerate(sudoku):
        print(f'{index}|  {sudoku[index][0]} {sudoku[index][1]} {sudoku[index][2]} | {sudoku[index][3]} {sudoku[index][4]}\
 {sudoku[index][5]} | {sudoku[index][6]} {sudoku[index][7]} {sudoku[index][8]}')
        if index in [2, 5]:
            print('-' * 26)
    print('    0 1 2   3 4 5   6 7 8')


def prava_stevilka(x, y, cifra, sudoku):
    """Preveri ali lahko na sudoku[x][y] postavimo cifro. Če je v isti vrstici ali
    v istem kvadratu, ali v istem stolpcu že ta cifra, potem vrne False, če ne pa vrne True."""
    stolpec = [sudoku[i][y] for i in range(0,9)]
    vrstica = sudoku[x]
    polje = {1: {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)},
             2: {(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)},
             3: {(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)},
             4: {(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)},
             5: {(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)},
             6: {(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)},
             7: {(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)},
             8: {(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)},
             9: {(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)}
             }
    if cifra in vrstica:
        return False
    elif cifra in stolpec:
        return False

    for st, koordinate in polje.items():
        if (x,y) in koordinate:
            for x1, y1 in polje[st]:
                if sudoku[x1][y1] == cifra:
                    return False

    return True


def prejsnja_koordinata(x, y, sudoku):
    if 1 <= y <= 8:
        sudoku[x][y-1] = 0

    elif y == 0:
        sudoku[x-1][8] = 0

    return sudoku


def rekurzija_sudoku(sudoku, i):
    for x in range(0,9):
        for y in range(0,9):
            if sudoku[x][y] == 0:
                for cifra in range(i,10):
                    if prava_stevilka(x,y,cifra,sudoku):
                        sudoku[x][y] = cifra
                        rekurzija_sudoku(sudoku, 1)
                else:
                    if 1 <= y <= 8:
                        cifra = sudoku[x][y - 1]
                    elif y == 0:
                        cifra = sudoku[x - 1][8]

                    sudoku = prejsnja_koordinata(x, y, sudoku)
                    rekurzija_sudoku(sudoku, cifra + 1)

            #if sudoku[x][y] != 0:
             #       sudoku = prejsnja_koordinata(x,y,sudoku)
              #      rekurzija_sudoku(sudoku, i+1)


    return sudoku









