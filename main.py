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
                if line.startswith("Sudoku"):  # siguiente sudoku encontrado
                    break
                tablero.append([int(char) for char in line])  # Convertimos cada número en entero
    return tablero

num = input()

tablero = cargar_tablero(num)

print(tablero)

for fila in tablero:
    print(" ".join(str(num) for num in fila))
