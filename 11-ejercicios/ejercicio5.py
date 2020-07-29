"""
Ejercicio 5.
Crear un lista con el contenido de esta tabla:
ACCION  AVENTURA            DEPORTES
GTA     ASSINS              Fifa 21
COD     CRASH               Pro 21
PUGB    Prince of Persia    MOTO GP 21

Mostrar esta información ordenada
"""

table = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "Call of Duty", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS", "Crash Bandicoot", "Prince of Persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PES 21", "MOTO GP 21"]
    }
]

for categoria in table:
    print(f"----------- {categoria['categoria']} ------------")

    for juego in categoria['juegos']:
        print(juego)