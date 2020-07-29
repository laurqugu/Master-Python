
def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

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