# Pida al usuario 5 números y diga si estos estaban en orden decreciente, creciente o desordenados.

#1. Definimos cómo debe ser una lista decreciente, creciente o desordenada mediante if, elif, else
#y qué debe retornar (en este caso, el print indicando qué tipo de lista es)
def state_list(a, b, c, d, e):
    if e > d and d > c and c > b and b > a:
       return print("La lista está ordenada de forma creciente")

    elif e < d and d < c and c < b and b < a:
       return print("La lista está ordenada de forma decreciente")

    else: 
       return print ("La lista está desordenada")

#2. Introducimos los valores mediante input de un número entero
a = int(input("Por favor, introduce un número: "))
b = int(input("Por favor, introduce un número: "))
c = int(input("Por favor, introduce un número: "))
d = int(input("Por favor, introduce un número: "))
e = int(input("Por favor, introduce un número: "))

#3. Llamamos a la función una vez introducidos los parámetros
state_list(a, b, c, d, e)
