"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre

Para acceder a esos valores podemos usar un indice numerico.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("Shakira", "Adele", "Denisse"))
years = list(range(2020, 2050))
variada = ["Laura", 27, 5.0, True, "Holi"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:1])
print(peliculas[2:])

# Añadir elementos a lista
cantantes.append("Leon Larregui")
cantantes.append("Cerati")
print(cantantes)

# Recorrer lista
print("\n********* LISTADO  PELICULAS *********\n")

nueva_pelicula = ""
"""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)
"""
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")

# Listas multidimensionales
print("\n***************** LISTADO DE CONTACTOS ******************")

contactos = [
    [
        'Antonio',
        'antonio@email.com'
    ],
    [
        'Cristobal',
        'cristobal@email.com'
    ],
    [
        'Laura',
        'laura@email.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#print(contactos[1][1])
