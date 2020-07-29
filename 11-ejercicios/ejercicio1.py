"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente
- Recorrer la lista y mostrarla
- Hacer función que recorra lista de numeros y devuelta un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (Que el usuario pida por teclado)
"""

# Crear Lista
numeros = [0, 4, 9, 1, 3, 6, 2, 7, 5, 8]

# Crear funcion que recorra Lista y devuelva string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    
    return resultado

# Recorrer y mostrar
print("***************** Recorrer y Mostrar ******************")

"""
for numero in numeros:
    print(numero)

"""

print(mostrarLista(numeros))


# Ordenar y mostrar
print("\n*************** Ordenar y Mostrar ***************")
numeros.sort()
print(numeros)

# Mostrar Longitud
print("\n*************** Mostrar longitud ***************")
print(len(numeros))

# Mostrar Elemento
print("\n*************** Busqueda en la lista***************")
elemento = int(input("Ingrese el número a buscar: "))

comprobar = isinstance(elemento, int)
while not comprobar or elemento <= 0:
    elemento = int(input("Ingrese el número a buscar: "))
else:
    print(f"Has introducido el {elemento}")

print(f"#### Buscar en la lista el número {elemento} ####")

search = numeros.index(elemento)

print(f"El número buscado existe en la lista, el es indice {search}")
