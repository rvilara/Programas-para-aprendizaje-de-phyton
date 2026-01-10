import random # Importa el módulo random para generar elecciones aleatorias

print("Bienvenido a Piedra, Papel o Tijera") # Mensaje de bienvenida al juego

opciones = ["piedra", "papel", "tijera"] # Define las opciones del juego
puntos_usuario = 0 # Inicializa el puntaje del usuario
puntos_computadora = 0 # Inicializa el puntaje de la computadora
rondas = 3 # Define el número de rondas a jugar

for i in range(rondas):
    print(f"\nRonda {i+1} de {rondas}") # Muestra el número de ronda actual
   
    usuario = input("Elige piedra, papel o tijera: ").lower() # Solicita la elección del usuario y la convierte a minúsculas
    while usuario not in opciones:
        print("Opcion no valida, intenta de nuevo ") # Mensaje de error si la opción no es válida
        usuario = input("Elige piedra, papel o tijera: ").lower() # Solicita nuevamente la elección del usuario 
    
    computadora = random.choice(opciones) # La computadora elige aleatoriamente una opción

#print("La computadora eligio: ", computadora) # Muestra la elección de la computadora

    if usuario == computadora: # Compara las elecciones para determinar si hay un empate
        print("Empate")
    elif (usuario == "piedra" and computadora == "tijera") or \
        (usuario == "papel" and computadora == "piedra") or \
        (usuario == "tijera" and computadora == "papel"): # Condiciones para que el usuario gane
        print("Ganaste!")
        puntos_usuario +=1 # Incrementa el puntaje del usuario
    else: 
        print("Perdiste!")
        puntos_computadora +=1 # Incrementa el puntaje de la computadora

print("\n --- Resultado final ---") # Muestra el resultado final después de todas las rondas
print("Puntos del usuario: ", puntos_usuario)
print("Puntos de la computadora: ", puntos_computadora)


if puntos_usuario > puntos_computadora:
    print("¡Felicidades! Has ganado el juego.") # Mensaje si el usuario gana
elif puntos_usuario < puntos_computadora:
    print("La computadora ha ganado el juego. ¡Mejor suerte la próxima vez!") # Mensaje si la computadora gana
else:
    print("Empate!") # Mensaje si hay un empate final      


