import random

def generar_coordenada_aleatoria():
    fila = random.randint(0, 9)         # Se está generando un número entero aleatorio del 0 al 9 para representar las filas del tablero
    columna = random.randint(0, 9)      # Se está generando un número entero aleatorio del 0 al 9 para representar las columnas del tablero
    return fila, columna                # Se retorna una tupla que contiene fila y columna al azar. Es decir, unas coordenadas.
