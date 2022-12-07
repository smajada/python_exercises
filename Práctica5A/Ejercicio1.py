#Sergio Majada Manresa
#1º DAW

# Creamos dos variables: una para la inserción de los números y la otra será nuestra lista.
palabra = input("Escribe una palabra: ")
lista = []

# Creamos una iteración que termine al escribir al insertar un valor vacío o, lo que es lo mismo, pulsar Enter. En ella,
# se insertará cada palabra que añadamos y pedirá una nueva hasta que se cumpla la condición.
while palabra != "":
    lista.append(palabra)
    palabra = input("Escribe una palabra: ")

# Por último, se imprime la lista.
print(f"Las palabras que has escrito son {lista}")
