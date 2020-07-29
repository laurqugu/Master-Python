"""
Ejercicio 5:
Hacer un programa que muestre todos los números entre 
dos números que diga el usuario.
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 <= num2:

    for cont in range(num1, (num2 + 1)):
        print(cont)

else: 
    print(f"El número {num1} debe ser menor al número {num2}")

