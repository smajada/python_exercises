# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura de un triángulo: 5
#     *
#    ***
#   *****
#  *******
# *********

# Creamos una variable que pedirá al usuario la altura del triángulo.
altura = int(input("Escribe la altura de tu triángulo: "))

# Por cada número de fila en el rango de la altura:
for n_fila in range(altura):
    # Imprimiermos tantos espacios vacíos como la altura que hemos marcado, menos el número de fila, menos 1 
    # y haremos que se imprima en horizontal
    print(" " * (altura - n_fila - 1), end="")
    #Luego, el print lo dividimos en tres:
        # 1. Se imprimen tantos "*" como el número de la fila en el que estamos, empezando por 0
        # 2. Se imprime un "*"
        # 3. Se imprimen tantos "*" como el número de la fila en el que estamos, empezando por 0
    print("*" * n_fila + "*" + "*" * n_fila, end="")
    # Por último, volveremos a imprimier tantos espacios vacíos como la altura que hemos marcado, menos el número de fila, menos 1
    print(" " * (altura - n_fila - 1))