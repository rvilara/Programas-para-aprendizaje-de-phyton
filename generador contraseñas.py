import random
import string

from sqlalchemy import true

def letras_minusculas(): 
    return ''.join(c for c in string.ascii_lowercase if c not in 'lo') #Devuelve las letras minusculas excluyendo l y o para evitar confusiones

def letras_mayusculas(): 
    return ''.join(c for c in string.ascii_uppercase if c not in 'IO') #Devuelve las letras mayusculas excluyendo I y O para evitar confusiones

def numeros(): #Devuelve los numeros
    return ''.join(c for c in string.digits if c not in '01') #Excluye 0 y 1 para evitar confusiones

def simbolos(): #Devuelve los simbolos
    return string.punctuation #Devuelve todos los simbolos disponibles

minimos = {"1": 2, "2": 3, "3": 4} #Define el minimo de caracteres segun la opcion elegida

while True: #Bucle para asegurar una opcion valida
    
    print("Opciones de contraseña:")
    print("1. Solo letras")
    print("2. Letras y numeros")
    print("3. Letras, numeros y simbolos")
    
    opcion = input("Elige una opcion (1, 2, 3): ")
    
    if opcion in ["1", "2", "3"]: #Verifica que la opcion sea valida
        break
    print("Opcion no valida. Por favor, elige 1, 2 o 3.\n")
    
while True: #Bucle para asegurar una longitud valida
    try:
        longitud = int(input(f"¿Cuantos caracteres quieres en tu contraseña? (minimo {minimos[opcion]}): "))
        
        if longitud >= minimos[opcion]:
            break
        else:
            print(f"Debes ingresas un numero mayor o igual a {minimos[opcion]}.")
    except ValueError: #Captura errores de conversion a entero
        print("Debes ingresas un numero valido.")
        
while True:
    try:
        cantidad = int(input("¿Cuántas contraseñas quieres generar? "))
        if cantidad > 0:
            break
        else:
            print("Debes ingresar un número mayor que 0.")
    except ValueError:
        print("Debes ingresar un número válido.")
        
def generar_contraseña(opcion, longitud): #Genera la contraseña segun la opcion y longitud
    password_forzada = [] #Lista para asegurar que se incluyan los tipos de caracteres necesarios
    caracteres = "" #Cadena que contendrá todos los caracteres posibles segun la opcion elegida

    if opcion =="1":
        caracteres = letras_minusculas() + letras_mayusculas()
        password_forzada.append(random.choice(letras_minusculas()))
        password_forzada.append(random.choice(letras_mayusculas()))
        nivel = "Debil"
    
    elif opcion =="2":
        caracteres = letras_minusculas() + letras_mayusculas() + numeros()
        password_forzada.append(random.choice(letras_minusculas()))
        password_forzada.append(random.choice(letras_mayusculas()))
        password_forzada.append(random.choice(numeros()))
        nivel = "Medio"
    
    elif opcion == "3":
        caracteres = letras_minusculas() + letras_mayusculas() + numeros() + simbolos()
        password_forzada.append(random.choice(letras_minusculas()))
        password_forzada.append(random.choice(letras_mayusculas()))
        password_forzada.append(random.choice(numeros()))
        password_forzada.append(random.choice(simbolos()))
        nivel = "Alto"
    
    restante = longitud - len(password_forzada) #Calcula los caracteres restantes
    password_restante = [random.choice(caracteres) for _ in range(restante)] #Genera los caracteres restantes
    password_final = password_forzada + password_restante #Combina ambas listas
    random.shuffle(password_final) #Para que no siempre esten al inicio los caracteres forzados
    contraseña = "".join(password_final) #Une la lista en una cadena
    return contraseña, nivel

#Genera la contraseña y obtiene el nivel de seguridad

for i in range(cantidad):
    pwd, nivel = generar_contraseña(opcion, longitud) #Genera la contraseña y obtiene el nivel de seguridad
    print(f"{i+1}. {pwd} (Nivel de seguridad: {nivel})") #Muestra la contraseña generada junto con su nivel de seguridad


