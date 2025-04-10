import os, time, random

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
    os.system('cls' if os.name == 'nt' else 'clear')

    print("╔════════════════════╗")
    print("║       Sudoku       ║")
    print("╚════════════════════╝")

    for i, fila in enumerate(tablero):
        fila_con_barras = []
        for j, val in enumerate(fila):
            fila_con_barras.append(val)
            if (j + 1) % 3 == 0 and j < 8:
                fila_con_barras.append("║")

        print(" ".join(fila_con_barras))

        if (i + 1) % 3 == 0 and i < 8:
            print("═" * 6 + "╬" + "═" * 7 + "╬" + "═" * 6)
    print()
            
def solucionar_sudoku(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == "-":
                for numero in range(1, 10):
                    if comprobar_tablero(tablero, fila, columna, numero):
                        tablero[fila][columna] = f"\033[31m{numero}\033[m"
                        imprimir_tablero(tablero)
                        time.sleep(0.3)
                        if solucionar_sudoku(tablero):
                            return True
                        tablero[fila][columna] = "-"
                return False
    return True

def comprobar_tablero(tablero, fila, columna, numero):
    # Fila
    if str(numero) in tablero[fila] or f"\033[31m{numero}\033[m" in tablero[fila]:
        return False
    
    # Columna
    for i in range(9):
        if tablero[i][columna] == str(numero) or tablero[i][columna] == f"\033[31m{numero}\033[m":
            return False

    # Cuadrante 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == str(numero) or tablero[i][j] == f"\033[31m{numero}\033[m":
                return False

    return True

tablero = cargar_tablero(random.randint(1, 4))

imprimir_tablero(tablero)
print(tablero)

solucionar_sudoku(tablero)
