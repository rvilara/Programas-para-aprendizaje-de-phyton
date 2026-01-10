# definimos funciones para cada operacion

print("Hola, la calculadora está funcionando")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b

# Funcion para mostrar el menu
def mostrar_menu():
    print("\n=== Calculadora Basica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Funcion principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una operacion (1 - 5): ")
        
        if opcion == "5":
            print("Saliendo de la calculadora.")
            break
        if opcion not in ["1", "2", "3", "4"]:
            print("Opcion no valida")
            continue
        
        try:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
        except ValueError:
            print("Por favor, ingresa un numero valido")
            continue
        
        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)
        
        print("El resultado es:", resultado)

# Llamamos a main solo cuando se ejecute el script directamente
if __name__ == "__main__":
    main()
