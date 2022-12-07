# Escribe un programa que pida un número y calcule su factorial.

n = int(input("Escribe un número:"))

# Se crea una variable de apoyo para multiplicar cada uno de los elementos de i
factorial = 1

# por cada i en el rango entre 1 y n+1
for i in range(1, n + 1):
    # La variable será igual a al misma variable * i
    factorial *= i
# Se imprime la variable factorial, que dará como resultado el factorial del numero
print(factorial)