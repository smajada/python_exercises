# Sergio Majada Manresa
# 1º DAW

# Creamos tres variables: una (num) a la que le introducimos el valor inicial, otra (apoyo) que nos servirá
# para guardar el valor de num cuando queramos comparar el anterior, y la variable de lista.
num = int(input("Escribe un número: "))
apoyo = 0
lista = []

# Mientras num sea mayor que la variable de apoyo:
# Añade el valor a la lista
# Guarda el valor de num en apoyo
# Cambia el valor de num por un nuevo input
while num > apoyo:
    lista.append(num)
    apoyo = num
    num = int(input(f"Escribe un número mayor que {apoyo}: "))


# Creamos una variable llamada string que posea el primer elemento de la lista
string = str(lista[0])

# Por cada elemento de la lista en un rango desde el segundo elemento (porque el primero ya está dentro de string)
# hasta el último elemento de la lista, que será marcado por el len()
# La variable string será la concatenación de string + una coma + el siguiente elemento de la lista transformado
# en string
for i in range(1, len(lista)):
    string += ", " + str(lista[i])

# Imprime la lista.
print(f"Los números que has escrito son: {string}")
