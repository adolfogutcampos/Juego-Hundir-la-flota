from clases_2 import Tablero
from funciones_3 import generar_coordenada_aleatoria

def imprimir_tablero_jugador(tablero):                              # Tablero del jugador "humano"
    print("\nTablero del jugador:")                                     # Encabezado que muestra el tablero del jugador "humano"
    for fila in range(tablero.dimensiones[0]):                      # Itera sobre cada fila y columna del tablero
        for columna in range(tablero.dimensiones[1]):               
            if tablero.tablero_con_barcos[fila, columna] == 1:      # Si hay un barco en la posición (fila, columna), se muestra como "B"
                print("B", end=" ")                                     # para representar casilla en la que hay un barco.
            elif tablero.tablero_impactos[fila, columna] == 1:      # Si no hay un barco, pero la casilla ha sido impactada por un disparo, se muestra como "F"
                print("F", end=" ")                                     # para representar una casilla que ha sido impactada
            elif tablero.tablero_impactos[fila, columna] == -1:     # Si la casilla ha sido impactada pero no había barco:
                print("A", end=" ")                                      # "A" de Agua para representar casilla impactada por agua
            else:                                                   # Si no se cumplen las condiciones anteriores, es que la casilla está vacía y se imprime "O" para representar una casilla vacía.
                print("O", end=" ")  
        print()  

def imprimir_tablero_maquina(tablero):                              # Tablero del jugador "máquina"
    print("\nTablero de la máquina:")                               
    for fila in range(tablero.dimensiones[0]):
        for columna in range(tablero.dimensiones[1]):
            if tablero.tablero_impactos[fila, columna] == 0:
                print("O", end=" ")                                 # Casilla oculta. En el tablero de la máquina no se muestran lógicamente las casillas.
            elif tablero.tablero_impactos[fila, columna] == 1:
                print("F", end=" ")                                 # Casilla impactada en barco enemigo con "F"
            else:
                print("A", end=" ")                                 # Casilla impactada por agua con "A"
        print()

def main():                                                             # Función principal
    print("¡Bienvenido a Hundir la Flota!")                             # Se imprime mensaje de bienvenida al ejecutar

    # Comenzar con el tablero del jugador "humano"
    tablero_jugador = Tablero(id_jugador="Jugador")                                     
    tablero_jugador.inicializar_tablero()

    # Permitir al jugador "humano" posicionar los barcos
    print("Coloca tus barcos en las coordenadas, recuerda las instrucciones para cada barco:")  # Poca importancia,sirve como introducción 
    for barco, posiciones in tablero_jugador.barcos.items():
        print(f"Posiciona el barco {barco}:")                           # Especifica por cada tipo de barco (lancha1, lancha2 etc)
        for i in range(len(posiciones)):
            fila, columna = posiciones[i]
            print(f"Posición {i + 1}: fila {fila}, columna {columna}")
        imprimir_tablero_jugador(tablero_jugador)                       # Mostrar tablero después de posicionar cada barco

    # Comenzar con el tablero del jugador "máquina"
    tablero_maquina = Tablero(id_jugador="Máquina") 
    tablero_maquina.inicializar_tablero()

    # Bucle principal while del juego
    turno = 1
    while True:
        # Mostrar turno actual de juego
        print("\n----- Turno", turno, "-----")      # Gracias a esto, se mostrará cada turno en qué turno va la partida, gracias a un contador

        # Turno del jugador "humano"
        print("\n¡Es tu turno!")
        imprimir_tablero_maquina(tablero_maquina)                           # Mostrar tablero del jugador "máquina"
        imprimir_tablero_jugador(tablero_jugador)                           # Mostrar tablero del jugador "humano"
        fila = int(input("Introduce la fila para disparar (0-9): "))        # En primer lugar, se escoge numero de fila del 0 al 9
        columna = int(input("Introduce la columna para disparar (0-9): "))  # En segundo lugar, se escoge columna del 0 al 9
        if tablero_maquina.disparo_coordenada(fila, columna):               # Si coincide coordenada con la de una casilla con barco enemigo
            print("¡Has impactado un barco!")
        else:
            print("¡Agua!")                                                 # Si NO coincide coordenada con la de una casilla con barco enemigo    

        # Verificar si el jugador "máquina" ha perdido
        if not 1 in tablero_maquina.tablero_con_barcos:                                     # Si Jugador "humano" gana...
            print("¡Has ganado la partida! El jugador máquina se ha quedado sin barcos.")
            break

        # Turno del jugador "máquina"
        print("\nAhora es el turno de la máquina...")                                       # En cada turno, dar paso a turno de la máquina
        fila, columna = generar_coordenada_aleatoria()
        if tablero_jugador.disparo_coordenada(fila, columna):
            print("Jugador máquina ha impactado uno de tus barcos en la fila", fila, "y columna", columna)
        else:
            print("Jugador máquina ha disparado al agua en la fila", fila, "y columna", columna)

        # Verificar si el jugador "humano" ha perdido
        if not 1 in tablero_jugador.tablero_con_barcos:                                     # Si jugador "máquina" ha ganado    
            print("¡Has perdido! La máquina ha hundido todos tus barcos.")                  
            break

        # Incrementar el turno
        turno += 1        # suma un turno por cada turno que pasa                                

if __name__ == "__main__":
    main()



