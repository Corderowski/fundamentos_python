def clasificar_nota(nota):
    """Retorna la categoría de la nota."""
    if nota >= 90:
        return "Excelente"
    elif nota >= 75:
        return "Bueno"
    elif nota >= 60:
        return "Suficiente"
    else:
        return "Reprobado"


# Usar la función con varias notas
suma  = 0
total = 0
with open("H:\Universidad\Github\fundamentos_python\03_listas_condiciones\notas_ejemplo.csv") as archivo:
    next(archivo) 
    for linea in archivo:
        partes = linea.strip().split(",")
        nota   = float(partes[1])
        suma  += nota
        total += 1

print(f"Promedio del salón (desde archivo): {suma/total:.2f}")

for nota in notas_prueba:
    categoria = clasificar_nota(nota)
    print(f"Nota {nota} → {categoria}")