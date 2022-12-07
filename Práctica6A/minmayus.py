# Sergio Majada Manresa
# 1º DAW

# Creamos un procedimiento, por lo que no retorna un valor, que imprime el texto en minúsculas y en mayúsculas
def min_mayus(texto):
    print(texto.lower())
    print(texto.upper())

# Introducimos una frase y llamamos al procedimiento
texto = str(input('Introduce una frase: '))
min_mayus(texto)
