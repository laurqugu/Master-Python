"""
Ejercicio 10.

El programa debe pedir la nota de 15 alumnos y sacar 
por pantalla cuantos han aprobado y cuantos han suspendido.
"""

cont = 0
aprobados = 0
suspendidos = 0

num_alumnos = int(input("¿Cuántos alumnos tienes? "))

while cont <= num_alumnos:
    nota = int(input(f"¿Qué notas quieres ponerle al \"alumno {cont}\"? "))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    cont += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"\nAlumnos suspendidos: {suspendidos}")

