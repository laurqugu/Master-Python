"""
Ejercicio 2:
-Escribir un script que nos muestre por pantalla todos lo numeros
pares del 1 al 120

"""

cont = 1

for cont in range(1, 121):
    if cont%2 == 0:
        print(f"{cont} es par")
    else:
        print(f"{cont} es impar")