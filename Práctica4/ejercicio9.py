# Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 4
# *****
# *   *
# *   *
# *****

# Guardamos las variables ancho y altura
ancho = int(input('Escribe el ancho de tu rectángulo: '))
altura = int(input('Escribe la altura de tu rectángulo: '))

# En la primera línea, imprimimos tantas "*" en horizontal como ancho hayamos guardado
for i in range(ancho):
    print('*', end='')
# Usamos este print para bajar de línea
print()

# En esta porción de código, se programa la parte central de nuestro rectángulo:
    # por cada i en altura - 2 (porque esas dos líneas deben estar completas) se imprime un "*" en horizontal
for i in range(altura - 2):
    print('*', end='')
    # Por cada número en el rango de ancho - 2 (porque esas dos columnas deben estar completas), se imprimirá un espacio en horizontal
    for j in range (ancho - 2):
        print(' ', end='')
    # Imprimimos un "*" para indicar que se ha acabado la línea
    print('*')
    
# En la primera línea, imprimimos tantas "*" en horizontal como ancho hayamos guardado
for i in range(ancho):
    print('*', end='')