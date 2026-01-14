import json

#variables globales

inventario = []

#persistencia de datos

def guardar_inventario():
    with open("inventario.json", "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False, indent=4)
        
def cargar_inventario():
    global inventario
    try:
        with open("inventario.json", "r", encoding="utf-8") as f:
            inventario = json.load(f)
    except FileNotFoundError:
        inventario = []
        
#funciones de validacion

def pedir_nombre():
    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre.replace("", "").isalpha():
            return nombre.title()
        else:
            print("Error: Solo letras y espacios")
            
def pedir_precio():
    while True:
        try:
            precio = float(input("Precio: "))
            if precio > 0:
                return precio
            else:
                print("Ingresa numero valido")
        except ValueError:
            print("Ingresa un numero valido")
                
def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser mayor que 0")
        except ValueError:
            print("Ingresa un numero entero valido")
            
#funciones CRUD

def agregar_producto():
    print("Agregar producto")
    nombre = pedir_nombre()
    precio = pedir_precio()
    cantidad = pedir_cantidad()
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }   
    
    inventario.append(producto)
    guardar_inventario()
    print("Producto agregado correctamente")

def mostrar_inventario():
    print ("Inventario")
    if not inventario:
        print("Inventario vacio")
        return
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. {producto['nombre']} | Precio: €{producto['precio']} | Cantidad: {producto['cantidad']}")
        
def buscar_producto():
    print("Buscar producto")
    termino = input("Buscar por nombre: ").lower()
    encontrados = False
    
    for producto in inventario:
        if termino in producto["nombre"].lower():
            print(f"{producto['nombre']} | Precio: €{producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrados = True
    if not encontrados:
        print("No se han encontrado productos")
        
def actualizar_producto():
    print("Actualizar producto")
    nombre = input("Nombre del producto a actualizar: ").lower()
    
    for producto in inventario:
        if nombre == producto["nombre"].lower():
            print("Producto encontrado")
            producto["precio"] = pedir_precio()
            producto["cantidad"] = pedir_cantidad()
            guardar_inventario()
            print("Producto actualizado")
            return
    print("Produccto no encontrado")
    
def eliminar_producto():
    print("Eliminar producto")
    nombre = input("Nombre del producto a eliminar: ").lower()
    
    for producto in inventario:
        if nombre == producto["nombre"].lower():
            inventario.remove(producto)
            guardar_inventario()
            print("Producto eliminado")
            return
    print("Producto no encontrado")
    
# funciones extras

def valor_total_inventario():
    total = sum(p["precio"]*p["cantidad"] for p in inventario)
    print(f"\n Valor total del inventario: €{total:.2f}")
    
# Menu principal

def menu():
    cargar_inventario()
    
    while True:
        print("""
              ---Mini inventario ---
              1. Agregar producto
              2. Mostrar inventario
              3. Buscar producto
              4. Actualizar inventario
              5. Eliminar producto
              6. Valor total del inventario
              7. Salir
              """)
        
        opcion = input("Seleciona una opcion (1-7): ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            valor_total_inventario()
        elif opcion == "7":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida, ingrese valor entre 1 y 7")
            
# Inicio del programa

menu()