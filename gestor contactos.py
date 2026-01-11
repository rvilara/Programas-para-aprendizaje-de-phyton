import json
agenda = [] # Lista para almacenar los contactos

def cargar_agenda(): # Función para cargar la agenda desde un archivo JSON
    global agenda # Usar la variable global agenda
    try: # Intentar abrir el archivo agenda.json
        with open("agenda.json", "r", encoding="utf-8") as f: # Abrir el archivo en modo lectura
            agenda = json.load(f) # Cargar la agenda desde el archivo JSON
    except FileNotFoundError: # Si el archivo no existe
        agenda = [] # Inicializar la agenda como una lista vacía

def mostrar_menu():
    print("Gestor de Contactos")
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def añadir_contacto(): # Función para añadir un nuevo contacto a la agenda
    while True:
        nombre = input("nombre: ").strip() # Leer los detalles del contacto
        if all(c.isalpha() or c.isspace() for c in nombre) and nombre != "": # Validar el nombre
            break
        print("El nombre solo puede contener letras y espacios.")
    while True:
        telefono = input("telefono: ").strip() # Leer los detalles del contacto
        if telefono.isdigit(): # Validar el telefono
            break
        print("El telefono solo puede contener numeros.")
    while True:
        mail = input("email: ").strip() # Leer los detalles del contacto
        if "@" in mail and "." in mail:
            break
        print("Introduce un email valido.")
        
        #nombre = pedir_nombre()
        #telefono = pedir_telefono()
        #email = pedir_email()
        
    contacto={ # Crear un diccionario para el contacto
        "nombre": nombre,
        "telefono": telefono,
        "email": mail
        }
    agenda.append(contacto) # Añadir el contacto a la lista de contactos
    guardar_agenda() # Guardar la agenda en el archivo JSON
    print("Contacto añadido correctamente.")

def ver_contactos(): # Función para ver todos los contactos en la agenda
    if not agenda: # Comprobar si la agenda está vacía
        print("No hay contactos en la agenda.")
        return
    for i, contacto in enumerate(agenda, start=1): # Iterar sobre los contactos y mostrarlos
        print(f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}") # Mostrar los detalles del contacto

def buscar_contacto(): # Función para buscar un contacto en la agenda
    if not agenda:
        print("No hay contactos en la agenda.")
        return
    
    busqueda = input("Introduce el nombre a buscar: ").strip().lower() # Leer el nombre a buscar
    encontrados = []
    
    for contacto in agenda: # Iterar sobre los contactos para buscar coincidencias
        if busqueda in contacto['nombre'].lower(): # Comprobar si el nombre coincide
            encontrados.append(contacto) # Añadir el contacto a la lista de encontrados
            
    if encontrados: # Comprobar si se encontraron contactos
        print("Contactos encontrados:")
        for i, c in enumerate(encontrados, start=1):
            print(f"{i}. Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}") # Mostrar los detalles del contacto encontrado
    else:
        print("No se encontraron contactos con ese nombre.")
        
def eliminar_contacto(): # Función para eliminar un contacto de la agenda
    if not agenda:
        print("No hay contactos en la agenda.")
        return
    
    busqueda = input("Introduce el nombre del contacto a eliminar: ").strip().lower()
    encontrados = [c for c in agenda if busqueda in c['nombre'].lower()]
    
    if not encontrados:
        print("No se encontraron contactos con ese nombre.")
        return
    
    if len(encontrados) > 1:
        print("\n --- CONTACTOS ENCONTRADOS ---")
        for i, c in enumerate(encontrados, start=1):
            print(f"{i}. Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")
            
        while True:
            try:
                opcion=int(input("Elige el numero de contacto a eliminar: "))
                if 1 <=opcion <= len(encontrados):
                    contacto = encontrados [opcion - 1]
                    agenda.remove(contacto)
                    guardar_agenda()
                    print(f"Contacto {contacto['nombre']} eliminado correctamente.")
                    break
                else:
                    print(f"Elige un numero entre 1 y {len(encontrados)}.")
            except ValueError:
                print("Introduce un numero valido.")
    else:
        contacto = encontrados[0]
        agenda.remove(contacto)
        guardar_agenda()
        print(f"Contacto {contacto['nombre']} eliminado correctamente.")
    
def guardar_agenda(): # Función para guardar la agenda en un archivo JSON
    with open("agenda.json", "w", encoding="utf-8") as f: # Abrir el archivo en modo escritura
        json.dump(agenda, f, ensure_ascii=False, indent=4) # Guardar la agenda en formato JSON

def main():
    cargar_agenda() # Cargar la agenda al iniciar el programa
    
    while True: # Bucle principal del programa
        mostrar_menu()
        opcion = input("Seleccione una opción:").strip() # Leer la opción del usuario
        print("opcion seleccionada: ", opcion)
        
        if opcion == "1":
            añadir_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Saliendo del gestor de contactos.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
main() # Llamada a la función principal para iniciar el programa 
    