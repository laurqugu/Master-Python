"""
SET es un tipo de dato, para tener un coleccion de valores,
pero no tiene ni indice ni orden
"""

personas = {
    "Laura",
    "Juan",
    "Antonio",
    "Cristobal"
}
personas.add("Claudia")
personas.remove("Laura")

print(type(personas))
print(personas)