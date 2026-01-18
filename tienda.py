import json

inventario = [] #Inventario de tienda
clientes = [] #Clientes de la tienda
ventas = [] # Ventas de la tienda

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
        
def nombre_cliente():
    while True:
        nombre = input("Nombre del cliente: ").strip()
        if nombre.replace (" ", "").isalpha():
            return nombre.title()
        else:
            print("Introduce solo letras y espacios.")
    
def apellido_cliente():
    while True:        
        apellido = input("Introduce apellidos del cliente: ").strip()
        if apellido.replace (" ", "").isalpha():
            return apellido.title()
        else:
            print("Introduce solo letras y espacios.")

def telefono_cliente():
    while True:
        try:
            telefono = int(input("Introduce telefono del cliente: "))
            if telefono >0:
                return telefono
            else:
                print("Ingresa un numero valido: ")
        except ValueError:
            print("Ingresa un numero valido")
            
def email_cliente():
    while True:
        email = input("Introduce email del cliente: ").strip()
        if "@" in email and "." in email:
            return email
        print("Introduce un email valido")
        
            
def agregar_cliente():
    print("Agregar cliente")
    nombre = nombre_cliente()
    apellido = apellido_cliente()
    telefono = telefono_cliente()
    email = email_cliente()
    
    cliente = {
        "nombre" : nombre.title(),
        "apellido" : apellido.title(),
        "telefono" : telefono,
        "email" : email
    }
    
    clientes.append(cliente)
    print(f"Cliente {nombre} {apellido} añadido correctamente")
    
def mostrar_clientes():
    if not clientes:
        print("No hay clientes")
        return
    print("Clientes registrados:")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c['nombre']} {c['apellido']} - {c['telefono']}")
        
def nombre_producto():
    while True:
        try:
            nombre = input("Nombre de producto: ").strip()
            if nombre.replace(" ", "").isalpha():
                return nombre.title()
            print("Introduce solo letras y espacios")
        except ValueError:
            print("Introduce un nombre valido")
            
def precio_producto():
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio > 0:
                return round(precio,2)
            print("Introduce un precio valido.")
        except ValueError:
            print("Introduce un numero valido.")
            
def stock_producto():
    while True:
        try:
            stock = int(input("Introduce cantidad de stock: "))
            if stock > 0:
                return stock
            print("Introduce un numero valido.")
        except ValueError:
            print("Introduce un numero valido.")
            
def agregar_producto():
    print("Agregar producto")
    nombre = nombre_producto()
    precio = precio_producto()
    stock = stock_producto()
    
    producto = {
        "nombre" : nombre,
        "precio" : precio,
        "stock" : stock
    }
    
    inventario.append(producto)
    guardar_inventario()
    print(f"Producto {nombre} añadido correctamente")
    
def mostrar_inventario():
    if not inventario:
        print("No hay productos en inventario")
        return
    print("\nInventario de productos")
    for i, p in enumerate(inventario,1):
        nombre = p.get("nombre", "SIN NOMBRE")
        precio = p.get("precio", 0)
        stock = p.get("stock", 0)
        print(f"{i}. {nombre} - {precio}€ - stock: {stock}")
            
def seleccionar_cliente():
    if not clientes:
        print("No hay clientes registrados")
        return None
    mostrar_clientes()
    while True:
        try:
            indice = int(input("Selecciona un cliente por numero: "))
            if 1 <= indice <= len(clientes):
                return clientes[indice -1]
            print("Numero de cliente invalido")
        except ValueError:
            print("Introduce un numero valido")
            
def seleccionar_producto():
    carrito = []
    if not inventario:
        print("No hay productos en inventario")
        return carrito
    while True:
        mostrar_inventario()
        try:
            indice = int(input("Selecciona un producto por numero (0 para terminar)"))
            if indice == 0:
                break
            if 1 <= indice <= len(inventario):
                producto = inventario[indice -1]
                if producto["stock"] == 0:
                    print("Producto sin stock")
                    continue
                cantidad = int(input(f"Cantidad de {producto['nombre']} (stock: {producto['stock']}):"))
                if 0 < cantidad <= producto["stock"]:
                    carrito.append({"producto": producto, "cantidad": cantidad})
                    producto["stock"] -= cantidad
                    guardar_inventario()
                else:
                    print("Cantidad invalida")
            else:
                print("Numero de producto invalido")
        except ValueError:
            print("Introduce un numero valido")
    return carrito

def registrar_venta():
    cliente = seleccionar_cliente()
    if not cliente:
        return
    carrito = seleccionar_producto()
    if not carrito:
        print("No se agregaron productos a la venta")
        return
    total = sum(item["producto"] ["precio"] * item["cantidad"] for item in carrito)
    
    venta = {
        "cliente" : cliente,
        "items" :[{"nombre":i["producto"]["nombre"], "cantidad": i["cantidad"], "precio_unit": i["producto"]["precio"]} for i in carrito],
        "total" : round(total, 2)
    }
    ventas.append(venta)
    guardar_ventas()
    print(f"Venta registrada. Total: {total} €")
    
def guardar_ventas():
    with open("ventas.json", "w", encoding="utf-8") as f:
        json.dump(ventas, f, ensure_ascii=False, indent=4)

def cargar_ventas():
    global ventas
    try:
        with open("ventas.json", "r", encoding="utf-8") as f:
            ventas = json.load(f)
    except FileNotFoundError:
        ventas = []
    
def mostrar_ventas():
    if not ventas:
        print("No se ha registrado ninguna venta")
        return
    for i, v in enumerate(ventas, 1):
        print(f"Venta {i} - Cliente: {v['cliente'] ['nombre']} {v['cliente'] ['apellido']}")
        for item in v["items"]:
            print(f" {item['cantidad']} x {item['nombre']} a {item['precio_unit']}€")
        print(f" Total: {v['total']}€\n")
        
def ingresos_totales():
    total = sum(v["total"] for v in ventas)
    print(f"Ingresos totales: {total}€")
    
def menu():
    cargar_inventario()
    cargar_ventas()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Agregar producto")
        print("4. Mostrar inventario")
        print("5. Registrar venta")
        print("6. Mostrar ventas")
        print("7. Ingresos totales")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            mostrar_ventas()
        elif opcion == "7":
            ingresos_totales()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    menu()