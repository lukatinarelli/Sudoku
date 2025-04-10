# 🧩 Solucionador de Sudokus en Python
Este es un proyecto personal para resolver sudokus de forma automática utilizando funciones recursivas en Python. Forma parte de un ejercicio propuesto por mi profesor de Fundamentos de Hardware (ASIR), donde también exploramos la recursividad con el clásico problema de las 8 damas.

## 🧠 ¿Qué hace el programa?
- Lee sudokus desde un archivo [sudoku.txt](sudoku.txt) con varios tableros escritos en un formato específico.
- Usa recursividad para probar combinaciones válidas en las casillas vacías.
- Muestra la evolución del tablero paso a paso con colores en terminal.
- Incluye comprobaciones de fila, columna y subcuadrante para cumplir las reglas del juego.

## 📁 Formato del archivo [sudoku.txt](sudoku.txt)
El archivo debe contener sudokus en este formato:
```
Sudoku 1:
000050000
000008470
001000600
010007000
906000700
000005000
320000060
000900020
600030004
Sudoku 2:
...
```
Donde **0** representa casillas vacías.

## 🖥️ Cómo usarlo
1. Asegúrate de tener **Python 3** instalado.
2. Coloca tu archivo _sudoku.txt_ en el mismo directorio del script.
3. Ejecuta el programa desde terminal:
```bash
python sudoku.py
```

## 🎨 Detalles visuales
- Las casillas originales del sudoku se mantienen sin color.
- Las casillas que el programa rellena se muestran en rojo con código ANSI (\033[31m), visible en terminales compatibles.
- El tablero se imprime con divisores (║, ═, ╔, etc.) para mejorar la legibilidad del cuadrante 3x3.

## 🔧 Cosas por mejorar
- Agregar validación de entrada para prevenir errores al cargar sudokus.
- Posibilidad de cargar o generar tableros aleatorios desde consola.
- Animaciones o interfaz gráfica (¿Tkinter o PyGame en el futuro?).

## 📜 Licencia

Este proyecto está publicado bajo la licencia Creative Commons Zero (CC0).  
Puedes usar, modificar y distribuir el código sin restricciones y sin necesidad de atribución.

[Ver licencia completa](LICENSE)
