# Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# ****
# ***
# **
# *


# Añadimos el número a la variable altura
altura = int(input('Escribe la altura de tu triángulo: '))

# por cada nº de línea en la que se encuentre entre la altura y 0, en orden decreciente
for n_linea in range(altura, 0, -1):
    # imprimir tantas "*" como el nº de línea en el que nos encontremos.
    print('*'*n_linea)