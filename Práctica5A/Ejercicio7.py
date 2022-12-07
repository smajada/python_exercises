#Sergio Majada Manresa
#1º DAW

# Creamos tres variables: límite, valores que se irán sumando y la lista en la que se irán insertando los valores.
limite = int(input("Escribe un número límite: "))
lista = []
suma = 0

# Mientras la suma de la los valores de la lista sea inferior al límite, los valores se
# irán añadiendo a la lista e irá pidiendo más nº para añadir.
while suma < limite:
    valor = int(input("Escribe un valor: "))
    lista.append(valor)
    suma += valor

#Creamos una variable llamada string que posea el primer elemento de la lista
string = str(lista[0])

# Por cada elemento de la lista en un rango desde el segundo elemento (porque el primero ya está dentro de string)
# hasta el último elemento de la lista, que será marcado por el len()
# La variable string será la concatenación de string + una coma + el siguiente elemento de la lista transformado en string
for i in range(1, len(lista)):
    string += ", " + str(lista[i])

# Imprimimos el resultado
print(
    f"El límite a superar es {limite}. La lista creada es {string} ya que la suma de estos números es {suma}."
)
