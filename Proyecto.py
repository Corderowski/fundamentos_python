import json
import os

ARCHIVO = "datos_fit.json"

# ------------------ FUNCIONES ------------------

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"usuario": {}, "ejercicios": []}


def guardar_datos(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)


def registrar_usuario(datos):
    print("\n--- Registro de Usuario ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    datos["usuario"] = {
        "nombre": nombre,
        "edad": edad,
        "peso": peso,
        "altura": altura
    }

    guardar_datos(datos)
    print("Usuario registrado.\n")


def registrar_ejercicio(datos):
    print("\n--- Registrar Ejercicio")
    tipo = input("Tipo de ejercicio: ")
    repeticiones = int(input("Repeticiones: "))
    peso = float(input("Peso usado (kg, 0 si no aplica): "))

    ejercicio = {
        "tipo": tipo,
        "repeticiones": repeticiones,
        "peso": peso
    }

    datos["ejercicios"].append(ejercicio)
    guardar_datos(datos)

    print("Ejercicio guardado.\n")


def ver_rutina(datos):
    print("\n--- Rutina de Ejercicios ---")

    usuario = datos["usuario"]
    if not usuario:
        print("No hay datos de usuario.\n")
        return

    print(f"Nombre: {usuario['nombre']}")
    print(f"Edad: {usuario['edad']}")
    print(f"Peso: {usuario['peso']} kg")
    print(f"Altura: {usuario['altura']} m")

    print("\nEjercicios realizados:")
    if not datos["ejercicios"]:
        print("No hay ejercicios registrados.\n")
        return

    for i, ej in enumerate(datos["ejercicios"], 1):
        print(f"{i}. {ej['tipo']} - {ej['repeticiones']} reps - {ej['peso']} kg")

    print()


# ------------------ MENÚ ------------------

def menu():
    datos = cargar_datos()

    while True:
        print("=== APP FITNESS ===")
        print("1. Registrar usuario")
        print("2. Registrar ejercicio")
        print("3. Ver rutina")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(datos)
        elif opcion == "2":
            registrar_ejercicio(datos)
        elif opcion == "3":
            ver_rutina(datos)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")

menu()