"""
# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras condiciones

# Operadores de comparacion
== igual
!= difiere
< menor que
> mayor que 
<= menor o igual que
>= mayor o igual que

# Operadores lógicos
and Y
or O
not no

"""

# Ejemplo 1
print("############# EJEMPLO 1 ############")

#color = input("Adivina cuál es mi color favorito: ")
color = "rojo"

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("El color NO es ROJO")


# Ejemplo 2
print("\n############# EJEMPLO 2 ############")

year = 2020
#year = int(input("¿En qué año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")


# Ejemplo 3
print("\n############# EJEMPLO 3 ############")

nombre = "Laura Quinchia"
ciudad = "Medellin"
continente = "America"
edad = 26
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "America":
        print("El usuario NO es americano")
    else:
        print(f"Es americano y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")


# Ejemplo 4
print("\n############# EJEMPLO 4 ############")

#dia = int(input("Introduce el día de la semana: "))
dia = 2

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

# Ejemplo 5
print("\n############# EJEMPLO 5 ############")

edad_minima = 18
edad_maxima = 65
edad_oficial = 26
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")


# Ejemplo 6
print("\n############# EJEMPLO 6 ############")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es de habla hispana")
else:
    print(f"{pais} no es de habla hispana")


# Ejemplo 7
print("\n############# EJEMPLO 7 ############")

pais = "Colombia"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es de habla hispana")
else:
    print(f"{pais} SI es de habla hispana")


# Ejemplo 7
print("\n############# EJEMPLO 7 ############")

pais = "EEUU"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es de habla hispana")
else:
    print(f"{pais} SI es de habla hispana :) ")
