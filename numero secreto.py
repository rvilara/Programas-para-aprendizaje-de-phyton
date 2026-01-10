import random
intentos = 3 # numero de intentos permitidos

numero_secreto = random.randint(1,10)  # define el numero a adivinar

print("Bienvenido al juego del numero secreto")  # mensaje de bienvenida

while intentos > 0:
    respuesta = int(input ("ingresa un numero del 1 al 10: "))  # lee la respuesta del usuario

    if respuesta == numero_secreto:
        print("Felicidades! Has adivinado el numero secreto.")  # mensaje de exito
        break
    else:
        intentos -= 1
        if respuesta < numero_secreto:
            print ("El numero es mayor")  # pista para el usuario
        elif respuesta > numero_secreto:
            print ("El numero es menor")  # pista para el usuario

if intentos == 0:
    print ("Has agotado todos tus intentos. El numero secreto era", numero_secreto)  # mensaje de fin del juego
    
