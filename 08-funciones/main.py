"""
FUNCIONES:

Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a 
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1

print("#### EJEMPLO 1 ####\n")

# Definir funciónn
def muestraNombre():
    print("Laura")
    print("Juliana")
    print("Antonio")
    print("Cristóbal")
    print("\n")

#Invocar función
muestraNombre()

# Ejemplo 2
print("#### EJEMPLO 2 ####\n")
"""
def mostrarTuNombre(nombre):
    print(f"Tu nombre es: {nombre}")

nombre = input("Introduce tu nombre: ")
mostrarTuNombre(nombre)
"""

# Ejemplo 3
print("#### EJEMPLO 3 ####\n")

#Definimos la función "Tabla"
def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for cont in range(11):
        operacion = numero * cont
        print(f"{numero} x {cont} = {operacion}")

    print("\n")
 
 #Invocamos la función y le enviamos como parámetro el número de la tabla que queremos calcular
tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1

print("------------------------------------------\n")
for num_tabla in range(1, 11):
    tabla(num_tabla)

#Ejemplo 4
print("#### EJEMPLO 4 ####\n")

# Parametros opcionales

def getEmpleado(nombre, id = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if id != None:
        print(f"Identific ación: {id}")

getEmpleado("Laura Quinchia")

# Ejemplo 5 - Return o devolver datos
print("\n#### EJEMPLO 5 ####\n")
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Laura Quinchia"))

# Ejemplo 6
print("\n#### EJEMPLO 6 ####\n")

def calculadora(num1, num2, basicas = False):
    
    suma = num1 + num2
    resta = num2 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(56, 5, False))

# Ejemplo 7
print("\n#### EJEMPLO 7 ####\n")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Laura", "Quinchia Gutierrez"))

# Ejemplo 8
print("\n#### EJEMPLO 8 ####\n")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2020))



