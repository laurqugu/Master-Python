"""
Ejercicio 9

Hacer un programa que pida números al usuario indefinidamente
hasta meter el número 111
"""

cont = 1

while cont < 100:
    num = int(input("Introduce un número: "))

    if num == 111:
        break
    else:
        print(f"Has introducido el {num}")