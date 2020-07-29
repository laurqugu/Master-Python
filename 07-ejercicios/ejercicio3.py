"""
Ejercicio 3:
Escribir un programa que muestre los cuadrados
(un número multiplicado por si mismo) de los 60 primeros números
naturales. Resolverlo con for y con while
"""

# WHILE

"""
cont = 0

while cont <= 60:

    cuadrado = cont * cont
    print(f"El cuadrado de {cont} es {cuadrado}")

    cont +=1

"""

# FOR
for num in range(61):
    cuadrado = num * num
    print(f"El cuadrado de {num} es {cuadrado}")
