# ----- CLASE -----
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def mostrar(self):
        print(f"{self.nombre} - {self.telefono} - {self.email}")

# ----- FUNCIONES -----
agenda = []

def cargar_agenda():
    global agenda
    agenda = []
    try:
        with open("agenda.txt", "r", encoding="utf8") as f:
            for linea in f:
                nombre, telefono, email = linea.strip().split("|")
                contacto = Contacto(nombre, telefono, email)
                agenda.append(contacto)
    except FileNotFoundError:
        agenda = []

def guardar_agenda():
    with open("agenda.txt", "w", encoding="utf8") as f:
        for contacto in agenda:
            f.write(f"{contacto.nombre}|{contacto.telefono}|{contacto.email}\n")

def añadir_contacto():
    nombre = input("Nombre: ").strip()
    telefono = input("Telefono: ").strip()
    email = input("Email: ").strip()
    contacto = Contacto(nombre, telefono, email)
    agenda.append(contacto)
    guardar_agenda()
    print(f"Contacto {nombre} añadido correctamente")

def ver_agenda():
    if not agenda:
        print("La agenda está vacía")
        return
    for i, contacto in enumerate(agenda, start=1):
        print(f"{i}. ", end="")
        contacto.mostrar()

def buscar_contacto():
    if not agenda:
        print("La agenda está vacía")
        return
    busqueda = input("Introduce el nombre a buscar: ").strip().lower()
    encontrados = [c for c in agenda if busqueda in c.nombre.lower()]
    if encontrados:
        print("Contactos encontrados:")
        for i, c in enumerate(encontrados, start=1):
            print(f"{i}. ", end="")
            c.mostrar()
    else:
        print("No se encontraron contactos con ese nombre.")
        

def editar_contacto():
    """Editar un contacto existente por nombre"""
    if not agenda:
        print("La agenda está vacía")
        return

    busqueda = input("Introduce el nombre del contacto a editar: ").strip().lower()
    encontrados = [c for c in agenda if busqueda in c.nombre.lower()]

    if not encontrados:
        print("No se encontraron contactos con ese nombre.")
        return

    # Si hay varios contactos coincidentes
    if len(encontrados) > 1:
        print("\n--- CONTACTOS ENCONTRADOS ---")
        for i, c in enumerate(encontrados, start=1):
            print(f"{i}. ", end="")
            c.mostrar()
        while True:
            try:
                opcion = int(input("Elige el número de contacto a editar: "))
                if 1 <= opcion <= len(encontrados):
                    contacto = encontrados[opcion - 1]
                    break
                else:
                    print(f"Elige un número entre 1 y {len(encontrados)}.")
            except ValueError:
                print("Introduce un número válido.")
    else:
        contacto = encontrados[0]

    print("\nDeja vacío si no deseas cambiar un campo.")
    nuevo_nombre = input(f"Nuevo nombre ({contacto.nombre}): ").strip()
    if nuevo_nombre:
        if all(c.isalpha() or c.isspace() for c in nuevo_nombre):
            contacto.nombre = nuevo_nombre
        else:
            print("Nombre no válido, se mantiene el anterior.")

    nuevo_telefono = input(f"Nuevo teléfono ({contacto.telefono}): ").strip()
    if nuevo_telefono:
        if nuevo_telefono.isdigit():
            contacto.telefono = nuevo_telefono
        else:
            print("Teléfono no válido, se mantiene el anterior.")

    nuevo_email = input(f"Nuevo email ({contacto.email}): ").strip()
    if nuevo_email:
        if "@" in nuevo_email and "." in nuevo_email:
            contacto.email = nuevo_email
        else:
            print("Email no válido, se mantiene el anterior.")

    guardar_agenda()
    print(f"Contacto {contacto.nombre} actualizado correctamente.")


def eliminar_contacto():
    if not agenda:
        print("La agenda está vacía")
        return
    busqueda = input("Introduce el nombre del contacto a eliminar: ").strip().lower()
    encontrados = [c for c in agenda if busqueda in c.nombre.lower()]
    if not encontrados:
        print("No se encontraron contactos con ese nombre.")
        return
    if len(encontrados) > 1:
        print("\n--- CONTACTOS ENCONTRADOS ---")
        for i, c in enumerate(encontrados, start=1):
            print(f"{i}. ", end="")
            c.mostrar()
        while True:
            try:
                opcion = int(input("Elige el número de contacto a eliminar: "))
                if 1 <= opcion <= len(encontrados):
                    contacto = encontrados[opcion - 1]
                    agenda.remove(contacto)
                    guardar_agenda()
                    print(f"Contacto {contacto.nombre} eliminado correctamente.")
                    break
                else:
                    print(f"Elige un número entre 1 y {len(encontrados)}.")
            except ValueError:
                print("Introduce un número válido.")
    else:
        contacto = encontrados[0]
        agenda.remove(contacto)
        guardar_agenda()
        print(f"Contacto {contacto.nombre} eliminado correctamente.")

# ----- MENÚ -----

def mostrar_menu():
    print("\n--- AGENDA PROFESIONAL ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Ver agenda")
    print("4. Eliminar contacto")
    print("5. Editar contacto")  
    print("6. Salir")


def main():
    cargar_agenda()  # Cargar agenda al iniciar
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()
        if opcion == "1":
            añadir_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            ver_agenda()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion =="5":
            editar_contacto()
        elif opcion == "6":
            print("Saliendo... ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
