"""
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenarla con texto y mostrarla en
mayusculas
"""

texto = " "

if len(texto.strip()) <= 0:
    # mostrar el texto
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")