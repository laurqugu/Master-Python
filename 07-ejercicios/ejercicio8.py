"""
Ejercicio 8:

¿Cuánto es el "x" por ciento de "x" número
"""

num = int(input("Introduce el número: "))
porcentaje = int(input(f"¿Qué porcentaje quiere sacar del {num}? "))

operacion = (num * (porcentaje/100))

print(f"El {porcentaje}% de {num} es: {operacion}")