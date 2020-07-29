"""
Variables locales: Se definen dentro de la función y no
se puede usar fuera de ella, solo están disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función 
y están disponibles dentro y fuera de ellas.
"""

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola Mundo"
    print("Dentro de la función")
    print(frase)

    year = 2020

    global website
    website = "laura.es"
    print("Dentro: ", website)

    return "Dato devuelto " + str(year)

print(holaMundo())
print("Fuera ", website)