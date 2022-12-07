# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# *
# **
# ***
# ****
# ***
# **
# *

# Añadimos el número a la variable altura
altura = int(input('Escribe la altura de tu triángulo: '))

# por cada número en el rango entre 1 y la altura 
for i in range(1, altura):
    #imprimimos tantos "*" como i
    print('*'*i)
# por cada numero entre la altura y 0, de forma decreciente
for i in range(altura, 0, -1):
    #imprimimos tantos "*" como i
    print('*'*i)
    