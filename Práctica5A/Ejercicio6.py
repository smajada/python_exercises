# Sergio Majada Manresa
# 1º DAW

# Se establecen 4 variables: un nº mínimo, uno máximo, una variable de apoyo y una lista.
min_num = int(input("Escribe un número: "))
max_num = int(input(f"Escribe un número mayor que {min_num}: "))
lista = []

# Comenzamos con el primer bucle que confirmará que el segundo nº es mayor que el primero.
# De no serlo, cambiará el valor de max_num por el nuevo introducido.
while max_num <= min_num:
    max_num = int(input(f"{max_num} no es mayor que {min_num}. Vuelve a probarlo: "))


inter_num = int(input(f"Escribe un número entre {min_num} y {max_num}: "))

# El loop insertará en la lista el nº entre el mín y el máx.
while (inter_num > min_num) and (inter_num < max_num):
    lista.append(inter_num)
    inter_num = int(input(f"Escribe un número entre {min_num} y {max_num}: "))

# Cuando al condición del loop ya no se cumpla, se imprimirá la lista.

# Creamos una variable llamada string que posea el primer elemento de la lista
string = str(lista[0])

# Por cada elemento de la lista en un rango desde el segundo elemento (porque el primero ya está dentro de string)
# hasta el último elemento de la lista, que será marcado por el len()
# La variable string será la concatenación de string + una coma + el siguiente elemento de la lista transformado en string
for i in range(1, len(lista)):
    string += ", " + str(lista[i])

# Imprimimos el resultado
print(
    f"Los números situados entre {min_num} y {max_num} que has escrito son: {string}"
)
