from sudoku import imprimir_tablero#, solucionar_sudoku, comprobar_tablero

tablero = [["-" if input() == "" else input() for _ in range(9)] for _ in range(9)]

imprimir_tablero(tablero)