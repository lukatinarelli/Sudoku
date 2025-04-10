import random

def cargar_tablero(num):
    tablero = []
    guardar = False
    with open("sudoku.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == f"Sudoku {num}:":
                guardar = True
                continue
            if guardar:
                if line.startswith("Sudoku"):
                    break
                fila = [char if char != "0" else "-" for char in line]
                tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    for i, fila in enumerate(tablero):
        fila_con_barras = []
        for j, val in enumerate(fila):
            fila_con_barras.append(val)
            if (j + 1) % 3 == 0 and j < 8:
                fila_con_barras.append("|")
        print(" ".join(fila_con_barras))
        if (i + 1) % 3 == 0 and i < 8:
            print("═" * 21)

def recorrer_sudoku(tablero):
    return True

tablero = cargar_tablero(random.randint(1, 10))

imprimir_tablero(tablero)
print(tablero)