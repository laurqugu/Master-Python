"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menos a 120 y luego mostrar la lista.
Plus: Usar While y For
"""

"""
coleccion = []

for contador in range(0, 120):
    coleccion.append(f"elemento-{contador}")
    print("Mostramos el: " + coleccion[contador])

print(coleccion[115])
"""

coleccion = []
cont = 0

while cont < 120:
    coleccion.append(f"elemento-{cont}")
    print("Mostrando el: " + coleccion[cont])
    cont += 1

print(coleccion[77])
