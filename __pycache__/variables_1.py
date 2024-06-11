# A continuación, se muestran las dimensiones del tablero.
# Tendremos que introducir el número de casillas por fila y columna. Por defecto, 10 filas y 10 columnas.
# Se da por hecho que para este juego, el número de filas y columnas tiene que tener el mismo valor numérico.

NUMERO_FILAS = 10
NUMERO_COLUMNAS = 10

# A continuación, se muestran las especificaciones de los barcos.
# Cada jugador puede poner 10 barcos en el tablero, repartidos en 4 tipos de barco:
    # Los barcos denominados "lancha" tienen 1 posición de eslora. Es decir, 1 casilla de largo.
    # Los barcos denominados "destructor" tienen 2 posiciones de eslora. Es decir, 2 casillas de largo.
    # Los barcos denominados "acorazado" tienen 3 posiciones de eslora. Es decir, 3 casillas de largo.
    # Los barcos denominados "portaviones" tienen 4 posiciones de eslora. Es decir, 4 casillas de largo.

# Las coordenadas empiezan por 0 hasta llegar al 9. No desde el 1 al 10.

# Para establecer cómo colocar la posición inicial de los barcos, se ha optado por introducirlas manualmente por coordenadas.
# Se pondrán dos ejemplos para comprender esto:
    # Ejemplo 1: Las lanchas sólo tienen una casilla, por lo que sólo hay que introducir:
        # Una coordenada x (horizontal, para línea)
        # Una coordenada y (vertical, para columna)
    # Ejemplo 2: Los destructores tienen 2 casillas, por lo que habría que introducir 2 coordenadas diferentes
        #Ambas coordenadas con su x e y, tienen que ser unidas de forma lineal.
        
BARCOS = {
    "lancha1": [(0, 0)],                                  
    "lancha2": [(0, 9)],
    "lancha3": [(9, 0)],
    "lancha4": [(9, 9)],
    "destructor1": [(0, 5), (0, 6)],                        
    "destructor2": [(3, 8), (3, 9)],
    "destructor3": [(9, 6), (9, 7)],
    "acorazado1": [(4, 1), (5, 1), (6, 1)],                 
    "acorazado2": [(1, 3), (2, 3), (3, 3)],
    "portaaviones": [(6, 3), (6, 4), (6, 5), (6, 6)]        
}
