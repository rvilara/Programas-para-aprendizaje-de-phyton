tablero = [ # Inicializacion del tablero
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def mostrar_tablero(tablero): # Función para mostrar el tablero
    for i, fila in enumerate(tablero):
        print(" | ".join(fila)) # Mostrar una fila del tablero
        if i < 2:
            print("---+---+---")
    print()

def pedir_movimiento(jugador, tablero): # Función para pedir el movimiento de un jugador
    while True: # Bucle hasta que se haga un movimiento válido
        try: # Intentar leer la fila y columna
            fila = int(input(f"jugador {jugador}, elige la fila (1-3): ")) - 1
            columna = int(input(f"jugador {jugador}, elige la columna (1-3): ")) - 1
            
            if fila not in range(3) or columna not in range(3): # Validar la fila y columna
                print("Error: fila y columna deben estar entre 1 y 3.")
                continue
            
            if tablero[fila][columna] != " ": # Comprobar si la celda está vacía
                print("Error: esa celda ya esta ocupada. Elige otra.")
                continue
            
            tablero[fila][columna] = jugador # Colocar la marca del jugador en la celda
            break
        except ValueError:  
            print("Error: debes introducir numero enteros.")

def hay_ganador(tablero, jugador): # Función para comprobar si hay un ganador
    for fila in tablero: # Comprobar filas
        if all(c == jugador for c in fila): 
            return True
        
    for col in range(3): # Comprobar columnas
            if all(tablero[fila][col] == jugador for fila in range(3)):
                return True
            
    if all(tablero[i][2 - i] == jugador for i in range (3)): # Comprobar diagonal principal
        return True
    
    return False # Comprobar diagonal secundaria
            
        

def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def main():
    tablero = [[" "]*3 for _ in range(3)]
    turno = "X"
    
    while True:
        mostrar_tablero(tablero)
        pedir_movimiento(turno, tablero)
        
        if hay_ganador(tablero, turno):
            mostrar_tablero(tablero)
            print(f"El jugador {turno} ha ganado!")
            break
        elif tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("Empate!")
            break
        
        turno = "0" if turno == "X" else "X"
        
main()