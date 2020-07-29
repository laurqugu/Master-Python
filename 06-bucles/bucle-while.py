"""

#BUCLE WHILE
Estructura de control que itera o repite la ejecución de una
serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condición.


while condicion:
    bloque de instrucciones
    actualización de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1

print("--------------------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

# Ejemplo

print("\n#### EJEMPLO ####")
num_usuario = int(input("¿De qué número quieres la tabla? "))

if num_usuario <1:
    num_usuario = 1

print(f"#### Tabla del {num_usuario} ####")

cont = 1

while cont <= 10:
    print(f"{num_usuario} x {cont} = {num_usuario*cont}")
    cont +=1
    