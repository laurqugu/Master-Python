"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear 
muchas variables y que cada una tenga un dato distinto.
"""

texto = "Máster en Python"
texto2 = "con Víctor Robles"
numero = 45
decimal = 6.7

print(texto)
print(texto2)
print(numero)
print(decimal)

print("---------------------------------------")

# Sustituir el valor de algunas variables / reasignado valores
numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("---------------------------------------")

# Concatenación
nombre = "Laura"
apellidos = " Quinchia"
web = "wwwwwww"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}") #También se puede aplicar en variables
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))