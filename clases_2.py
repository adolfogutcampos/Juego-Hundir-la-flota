import numpy as np
from variables_1 import NUMERO_FILAS, NUMERO_COLUMNAS, BARCOS

class Tablero:                                                  # Representar el tablero para un jugador

    def __init__(self, id_jugador):
        self.id_jugador = id_jugador                                        # id_jugador: identifica al jugador
        self.dimensiones = (NUMERO_FILAS, NUMERO_COLUMNAS)                  # dimensiones: representa dimensiones del tablero de 10x10
        self.tablero_con_barcos = np.zeros(self.dimensiones, dtype = int)   # array numpy con ceros. Representa tablero del jugador con ubicación de los barcos
        self.tablero_impactos = np.zeros(self.dimensiones, dtype = int)     # array numpy con ceros. Representa tablero del jugador con impactos de los disparos realizados por jugador "máquina"
        self.barcos = BARCOS                                                # Barcos: diccionario con posición de barcos en archivo variables_1

    def inicializar_tablero(self):                              # Método que inicializa el tablero del jugador "humano" con los barcos en sus posiciones
        for barco, posiciones in self.barcos.items():           
            for fila, columna in posiciones:
                self.tablero_con_barcos[fila, columna] = 1      # Se marcan las casillas correspondientes a los barcos en tablero_con_barcos como ocupadas

    def disparo_coordenada(self, fila, columna):                # Este método toma una coordenada de disparo teniendo en cuenta la fila y columna como entrada. Luego se determina si el disparo acierta a un barco del jugador "máquina". Luego actualiza los tableros de impactos. Devuelve con True si el disparo ha acertado, sino False. 
        if self.tablero_con_barcos[fila, columna] == 1:         
            self.tablero_con_barcos[fila, columna] = 2                      # Marcar como impacto, que luego será "F" de fuego.
            self.tablero_impactos[fila, columna] = 1
            return True                                                     # True, ha habido impacto
        else:
            self.tablero_impactos[fila, columna] = -1
            return False                                                    # False, no ha habido impacto

    def tablero_visible(self):
        return np.where(self.tablero_impactos == 0, " ", np.where(self.tablero_con_barcos == 1, "B", "O"))
    # Este método devuelve una representación del tablero que es visible para el jugador "humano".
    # Muestra
        # 1- las posiciones donde hay barcos con "B".
        # 2- las posiciones donde no hay barcos con "O"
        # 3- las posiciones que han sido atacadas por jugador "máquina" donde ha habido un impacto a un barco con "F" de Fuego
        # 4- las posiciones que han sido atacadas por jugador "máquina" donde NO ha habido un impacto a un barco con "A" de Agua