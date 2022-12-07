# Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 3
# *****
# *****
# *****

# Se piden las dos variables
ancho = int(input('Escribe el ancho de tu rectángulo: '))
altura = int(input('Escribe la altura de tu rectángulo: '))

# por cada i entre 0 y el número de la altura
for i in range(altura):
    # Se imprimen tantas "*" como el ancho que hemos indicado
    print('*'*ancho)