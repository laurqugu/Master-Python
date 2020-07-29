"""
Ejercicio 7

Hacer un programa que muestre todos los número impares entre
dos número que decida el usuario.
"""

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce el siguiente número: "))


if num1 < num2:
    
    for x in range(num1, (num2 + 1)):

        if x%2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")


else:
    print("El número 1 debe ser mayor al número 2")    
