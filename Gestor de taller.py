import json

# ==========================
# Variables globales
# ==========================
clientes = []
ordenes = []

# ==========================
# Clientes
# ==========================
def añadir_cliente():
    nombre = input("Nombre del cliente: ").strip()
    telefono = input("Teléfono: ").strip()
    cliente = {
        "nombre": nombre.title(),
        "telefono": telefono,
        "vehiculos": []
    }
    clientes.append(cliente)
    guardar_clientes()
    print("Cliente añadido correctamente.")

def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return
    for i, cliente in enumerate(clientes, start=1):
        print(f"\n{i}. {cliente['nombre']} - {cliente['telefono']} (Vehículos: {len(cliente['vehiculos'])})")
        for v in cliente.get("vehiculos", []):
            print(f"   • {v['matricula']} | {v['marca']} {v['modelo']}")

def eliminar_cliente():
    if not clientes:
        print("No hay clientes para eliminar.")
        return
    mostrar_clientes()
    idx = int(input("Selecciona cliente a eliminar: ")) - 1
    if idx < 0 or idx >= len(clientes):
        print("Cliente no válido.")
        return
    confirm = input(f"¿Seguro que quieres eliminar al cliente {clientes[idx]['nombre']}? (s/n): ").lower()
    if confirm == 's':
        del clientes[idx]
        guardar_clientes()
        print("Cliente eliminado.")

def guardar_clientes():
    with open("clientes.json", "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def cargar_clientes():
    global clientes
    try:
        with open("clientes.json", "r", encoding="utf-8") as f:
            clientes = json.load(f)
            for c in clientes:
                if "vehiculos" not in c:
                    c["vehiculos"] = []
    except FileNotFoundError:
        clientes = []

# ==========================
# Vehículos
# ==========================
def añadir_vehiculo():
    if not clientes:
        print("No hay clientes registrados.")
        return
    mostrar_clientes()
    idx = int(input("Selecciona cliente para añadir vehículo: ")) - 1
    if idx < 0 or idx >= len(clientes):
        print("Cliente no válido.")
        return
    matricula = input("Matrícula: ").upper()
    marca = input("Marca: ").title()
    modelo = input("Modelo: ").title()
    vehiculo = {"matricula": matricula, "marca": marca, "modelo": modelo}
    clientes[idx]["vehiculos"].append(vehiculo)
    guardar_clientes()
    print("Vehículo añadido correctamente.")

def eliminar_vehiculo():
    if not clientes:
        print("No hay clientes.")
        return
    mostrar_clientes()
    c_idx = int(input("Selecciona cliente: ")) - 1
    if c_idx < 0 or c_idx >= len(clientes):
        print("Cliente no válido.")
        return
    if not clientes[c_idx]["vehiculos"]:
        print("Este cliente no tiene vehículos.")
        return
    for i, v in enumerate(clientes[c_idx]["vehiculos"], start=1):
        print(f"{i}. {v['matricula']} | {v['marca']} {v['modelo']}")
    v_idx = int(input("Selecciona vehículo a eliminar: ")) - 1
    if v_idx < 0 or v_idx >= len(clientes[c_idx]["vehiculos"]):
        print("Vehículo no válido.")
        return
    confirm = input(f"¿Eliminar vehículo {clientes[c_idx]['vehiculos'][v_idx]['matricula']}? (s/n): ").lower()
    if confirm == 's':
        del clientes[c_idx]["vehiculos"][v_idx]
        guardar_clientes()
        print("Vehículo eliminado.")

# ==========================
# Órdenes de trabajo
# ==========================
def añadir_orden():
    if not clientes:
        print("No hay clientes.")
        return
    mostrar_clientes()
    c_idx = int(input("Selecciona cliente: ")) - 1
    if c_idx < 0 or c_idx >= len(clientes):
        print("Cliente no válido.")
        return
    if not clientes[c_idx]["vehiculos"]:
        print("Este cliente no tiene vehículos.")
        return
    for i, v in enumerate(clientes[c_idx]["vehiculos"], start=1):
        print(f"{i}. {v['matricula']} | {v['marca']} {v['modelo']}")
    v_idx = int(input("Selecciona vehículo: ")) - 1
    if v_idx < 0 or v_idx >= len(clientes[c_idx]["vehiculos"]):
        print("Vehículo no válido.")
        return
    descripcion = input("Descripción de la reparación: ").strip()
    orden = {
        "cliente": clientes[c_idx]["nombre"],
        "vehiculo": clientes[c_idx]["vehiculos"][v_idx]["matricula"],
        "descripcion": descripcion,
        "estado": "Pendiente"
    }
    ordenes.append(orden)
    guardar_ordenes()
    print("Orden añadida correctamente.")

def mostrar_ordenes():
    if not ordenes:
        print("No hay órdenes registradas.")
        return
    for i, o in enumerate(ordenes, start=1):
        print(f"{i}. Cliente: {o['cliente']} | Vehículo: {o['vehiculo']} | "
              f"Descripción: {o['descripcion']} | Estado: {o['estado']}")

def cambiar_estado_orden():
    if not ordenes:
        print("No hay órdenes.")
        return
    mostrar_ordenes()
    idx = int(input("Selecciona orden a actualizar: ")) - 1
    if idx < 0 or idx >= len(ordenes):
        print("Orden no válida.")
        return
    print("Estados disponibles: Pendiente, En proceso, Finalizada")
    estado = input("Nuevo estado: ").strip().title()
    if estado not in ["Pendiente", "En Proceso", "Finalizada"]:
        print("Estado no válido.")
        return
    ordenes[idx]["estado"] = estado
    guardar_ordenes()
    print("Estado actualizado.")

def eliminar_orden():
    if not ordenes:
        print("No hay órdenes.")
        return
    mostrar_ordenes()
    idx = int(input("Selecciona orden a eliminar: ")) - 1
    if idx < 0 or idx >= len(ordenes):
        print("Orden no válida.")
        return
    confirm = input(f"¿Eliminar la orden de {ordenes[idx]['cliente']}? (s/n): ").lower()
    if confirm == 's':
        del ordenes[idx]
        guardar_ordenes()
        print("Orden eliminada.")

def guardar_ordenes():
    with open("ordenes.json", "w", encoding="utf-8") as f:
        json.dump(ordenes, f, indent=4, ensure_ascii=False)

def cargar_ordenes():
    global ordenes
    try:
        with open("ordenes.json", "r", encoding="utf-8") as f:
            ordenes = json.load(f)
    except FileNotFoundError:
        ordenes = []

# ==========================
# Menú principal
# ==========================
def menu():
    while True:
        print("""
--- Gestor de Taller ---
1. Agregar cliente
2. Mostrar clientes
3. Eliminar cliente
4. Añadir vehículo
5. Eliminar vehículo
6. Añadir orden
7. Mostrar órdenes
8. Cambiar estado de orden
9. Eliminar orden
10. Salir
""")
        opcion = input("Selecciona una opción (1-10): ").strip()
        if opcion == "1":
            añadir_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            añadir_vehiculo()
        elif opcion == "5":
            eliminar_vehiculo()
        elif opcion == "6":
            añadir_orden()
        elif opcion == "7":
            mostrar_ordenes()
        elif opcion == "8":
            cambiar_estado_orden()
        elif opcion == "9":
            eliminar_orden()
        elif opcion == "10":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, ingrese un número entre 1 y 10.")

# ==========================
# Iniciar programa
# ==========================
cargar_clientes()
cargar_ordenes()
menu()