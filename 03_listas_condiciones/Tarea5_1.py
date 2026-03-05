
#Lista de notas
lista_notas = []

with open("notas_ejemplo.csv") as archivo:
    next(archivo) 
    
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        nota = float(datos[1])
        
        lista_notas.append(nota)

promedio = sum(lista_notas) / len(lista_notas)



def clasificar_nota(nota):
    if nota >= 90:
        return "Excelente"
    elif nota >= 75:
        return "Bueno"
    elif nota >= 60:
        return "Suficiente"
    else:
        return "Reprobado"

def reporte_salon(lista_notas):
    promedio = sum(lista_notas) / len(lista_notas)
    
aprobados = 0
reprobados = 0
eximidos = 0
    
for nota in lista_notas:
    if nota >=90:
        eximidos += 1
    elif nota >= 70:
        aprobados += 1
    else:
        reprobados += 1 
    

while True:
    print("\n--- Menú de Notas ---")
    print("1. Promedio")
    print("2. Eximidos")
    print("3. Nota mas alta")
    print("4. Nota mas baja")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        print(f"Los estudiantes presentan un promedio de: {promedio:.2f}")
    elif opcion == "2":
        print(f"Cantidad de estudiantes eximidos: {eximidos:}")
    elif opcion == "3":
        nota_alta = max(lista_notas)
        print(f"El estudiante con la nota mas alta fue {nombre} con una nota de {nota_alta:.2f}")
    elif opcion == "4":
        nota_baja = min(lista_notas)
        print(f"El estudiante con la nota mas baja fue {nombre} con una nota de {nota_baja:.2f}")
    
    elif opcion == "5":
        print("Cerrando programa...")
        break

    else:
        print("opcion invalida, intente de nuevo!")
