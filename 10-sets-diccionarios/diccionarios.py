"""
DICCIONARIO es un tipod e tdatoq ue almacena un conjunto de datos,
en formato clave > valor
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Laura",
    "apellidos": "Quinchia",
    "email": "laura@email.com"
}

print(persona["apellidos"])
print(type(persona))

# Lsita con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Cristobal',
        'email': 'cristobal@email.com'
    },
    {
        'nombre': 'Laura',
        'email': 'laura@laura.com'
    }
]

print(contactos[0]['nombre'])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------------------------------------")