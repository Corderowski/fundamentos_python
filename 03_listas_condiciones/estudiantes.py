def agregar_estudiante(estudiantes: list) -> None:
    """Solicita un nombre y lo agrega a la lista."""
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    if nombre:
        estudiantes.append(nombre)
        print(f"✅ Estudiante '{nombre}' agregado exitosamente.")
    else:
        print("❌ El nombre no puede estar vacío.")


def ver_lista(estudiantes: list) -> None:
    """Muestra todos los estudiantes numerados."""
    if not estudiantes:
        print("La lista está vacía.")
    else:
        for numero, estudiante in enumerate(estudiantes, start=1):
            print(f"{numero} - {estudiante}")


def ver_estudiante(estudiantes: list) -> None:
    """Muestra un estudiante por su número en la lista."""
    try:
        num = int(input("Ingrese el número del estudiante: "))
        print(f"Estudiante: {estudiantes[num - 1]}")
    except ValueError:
        print("❌ Ingrese un número válido.")
    except IndexError:
        print(f"❌ Número fuera de rango. Hay {len(estudiantes)} estudiante(s) registrado(s).")


# --- Programa principal ---
estudiantes = []

while True:
    print("\nSeleccione una opción:")
    print("1. Agregar nuevo estudiante")
    print("2. Ver la lista completa de estudiantes")
    print("3. Ver un estudiante en particular")
    print("4. Salir")

    opcion = input("Ingrese la opción: ")

    if opcion == "1":
        agregar_estudiante(estudiantes)
    elif opcion == "2":
        ver_lista(estudiantes)
    elif opcion == "3":
        ver_estudiante(estudiantes)
    elif opcion == "4":
        print("Cerrando el sistema...")
        break
    else:
        print("❌ Ingrese una opción válida.")
