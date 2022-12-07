# 1. Definimos una función para declarar el número mayor, utilizando if, elif y else
def num_mayor(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        return a

    elif b > a and b > c and b > d and b > e:
        return b

    elif c > a and c > b and c > d and c > e:
        return c

    elif d > a and d > b and d > c and d > e:
        return d

    else:
        return e

# 2. Definimos una función para declarar el número menor, utilizando if, elif y else
def num_menor(a, b, c, d, e):
    if a < b and a < c and a < d and a < e:
        return a

    elif b < a and b < c and b < d and b < e:
        return b

    elif c < a and c < b and c < d and c < e:
        return c

    elif d < a and d < b and d < c and d < e:
        return d

    else:
        return e


# 3. Pedimos al usuario que introduzca los números
a = int(input("Por favor, introduce un número: "))
b = int(input("Por favor, introduce un número: "))
c = int(input("Por favor, introduce un número: "))
d = int(input("Por favor, introduce un número: "))
e = int(input("Por favor, introduce un número: "))

# 4. Llamamos a las dos funciones (num_mayor y num_menor)
# 4.1 Declaramos dos variables para imprimir nuestra respuesta y no tener que poner la función y sus parámetros 
# (max_num y min_num son simples variables estéticas)
max_num = num_mayor(a, b, c, d, e)
min_num = num_menor(a, b, c, d, e)

# 5. Imprimimos la respuesta
print(f"El número mayor es {max_num} y el número menor es {min_num}")
