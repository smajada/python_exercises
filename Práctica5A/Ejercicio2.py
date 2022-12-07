#Sergio Majada Manresa
#1º DAW

# Creamos dos variables: una para la inserción de los números y la otra será nuestra lista.
#  La variable números pedirá al usuario que inserte números, pero no le indicaremos que el input sea un número entero,
# de esta manera podremos utilizar el comando "Salir" para terminar la iteración.
numeros = int(input("Escribe un número: "))
lista = []

# Creamos una iteración que termine al escribir "Salir". En ella,
# se insertará cada número que añadamos y pedirá uno nuevo hasta que se cumpla la condición.
while numeros != "Salir":
    numeros = int(numeros)
    lista.append(numeros)
    numeros = input("Escribe un número: ")

# Por último, se imprime la lista.
print(f"Los números que has escrito son: {lista}")
