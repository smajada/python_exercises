# Escribe un programa que escriba a los siguientes números (la separación entre número es para facilitar
# cuántos números se deben escribir en cada bucle) y en el que la función range que utilices tenga un ÚNICO
# argumento y que el valor de este se corresponda con el número de elementos que aparecen en la lista ( por Ejemplo,
# para la primera lista range (11)).

# Se imprime una lista de 10 números
for i in range(10):
    print(i + 1, end=" ")
print()

# Se imprimen 10 números con salto de 2
for i in range(10):
    print(i + 1 * 2, end=" ")
print()

# Se imprimen 10 números a partir de 20 con salto de 2
for i in range(10):
    print(i * 2 + 20, end=" ")
print()

# Se imprimen 6 números a partir de 10 con salto de 4
for i in range(6):
    print(i * 4 + 10, end=" ")
print()

# Se imprimen 9 números con salto de 5, de forma decreciente, desde 40
for i in range(9):
    print(-5 * i + 40, end=" ")