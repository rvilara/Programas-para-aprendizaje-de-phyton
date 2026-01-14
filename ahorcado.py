import random
guiones = []
letras_adivinadas = []
letras_incorrectas = []

racha = 0
print("Bienvenido al AHORCADO!")

#palabra = input("Introduce la palabra secreta: ").strip().lower()
palabras = ["python", "ahorcado", "programa", "juego", "consola", "coche", "ordenador", "casa", "apartamento", "moto"]
palabra = random.choice(palabras)

for letra in palabra:
    guiones.append("_")
    
intentos = 8

while intentos > 0 and "_" in guiones:
    print("Palabra:", " ".join(guiones))
    print("Intentos restantes: ", intentos)
    print("Letras usadas: ",letras_adivinadas)
    print("Letras incorrectas: ",letras_incorrectas)
    print("Racha de aciertos consecutivos: ",racha)

    letra = input("Introduce una letra: ").lower()

    if len(letra) !=1:
        print("Introduce una sola letra")
        
    if letra in letras_adivinadas:
        print("Ya has utilizado esa letra.")
        continue
    else:
        letras_adivinadas.append(letra)
    
    if not letra.isalpha():
        print("Introduce letra valida, no nummeros.")
        continue
    
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                guiones[i] = letra
        if letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
        else:
            print("Ya has utilizado esa letra antes")
        print("Buena, la letra esta en la palabra!")
        racha +=1
    else:
        print("La letra no se encuentra en la palabra")
        letras_incorrectas.append(letra)
        intentos-=1
        racha = 0 
    
if "_" not in guiones:
    print("Has ganado, la palabra secreta era: ",palabra)
else:
    print("Has perdido!, la palabra era: ",palabra)
    
    

