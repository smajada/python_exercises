# Sergio Majada Manresa
# 1º DAW

# Creamos tres variables: límite, valores que se irán sumando y la lista en la que se irán insertando los valores.
lista = []
limite = int(input("Escribe un número límite: "))
suma = 0

# Mientras la suma de la los valores de la lista sea inferior al límite, se irán
# pidiendo valores. Si el nuevo valor es mayor que el límite,
# se cambia el valor de la variable "valor" y se añade a
while suma < limite:
    valor = int(input("Escribe otro valor: "))
    if (valor + suma) > limite:
        print(f"{valor} es demasiado grande.")
    else:
        suma += valor
        lista.append(valor)

# Creamos una variable string que convierta el primer ítem de la lista en una string
string = str(lista[0])

# Por cada elemento de la lista en un rango desde el segundo elemento (porque el primero ya está dentro de string)
# hasta el último elemento de la lista, que será marcado por el len()
# La variable string será la concatenación de string + una coma + el siguiente elemento de la lista transformado en string
for i in range(1, len(lista)):
    string += ", " + str(lista[i])

# Cuando la condición se cumpla, imprimirá el resultado.
print(f"El límite a alcanzar es {limite}. La lista creada es {string}")
