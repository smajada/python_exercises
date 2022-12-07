# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# *
# **
# ***
# ****

# Añadimos el número a la variable altura
altura = int(input('Escribe la altura de tu triángulo: '))

# Por cada número entre 1 y la altura
for línea in range(1, altura):
    # Imprimimos tantas "*" como la línea en la que se encuentra
    print('*'*línea)