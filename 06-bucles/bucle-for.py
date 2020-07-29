"""
#FOR
for variable in elemento iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el "+ str(contador))

    resultado += contador


print(f"\nEl resultado es: {resultado}")

#Ejemplo tablas de multiplicar
print("\n########## EJEMPLO ##########")

num_usuario = int(input("¿De qué número quieres la tabla? "))

if num_usuario < 1:
    num_usuario = 1

print(f"\n### Tabla de multiplicar del número {num_usuario} ###")

for num_tabla in range(1, 11):
    
    if num_usuario == 45:
        print("No se pueden mostrar número prohibidos!!")
        break
    
    print(f"{num_usuario} x {num_tabla} = {num_usuario*num_tabla}")
else:
    print("\nTabla finalizada")
