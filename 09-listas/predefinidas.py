cantantes = ['Adele', 'Shakira', 'Denisse', 'Leon Larregui']
numeros = [1, 8, 9, 5, 3, 2, 4, 7, 6]

# Ordenar
#print(numeros)
numeros.sort()
#print(numeros)

# Añadir elementos
cantantes.append("Enrique Bunbury")
cantantes.insert(1, "Thalia")
#print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove('Shakira')
#print(cantantes)

# Dar la vuelta
#print(numeros)
numeros.reverse()
#print(numeros)

# Buscar dentro de una lista
#print('Denisse' in cantantes)

# Contar elementos
#print(cantantes)
#print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
#print(numeros.count(8))

# Conseguir indice
#print(cantantes.index('Denisse'))

# Unir listas
cantantes.extend(numeros)
print(cantantes)
