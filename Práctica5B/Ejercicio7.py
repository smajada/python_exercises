# Enunciado del programa: Tomando como entrada un número cualquiera, separa en dos listas los números pares
# y los impares que hay desde el 0 hasta ese número.

# Importamos la librería time para medir el tiempo de ejecución
import time

# Creamos tres variables: la que nos ayudará a introducir los números y dos listas: una de pares y otra de impares.
num = int(input("Introduce un número: "))
pares = []
impares = []

# Creamos una variable inicio que guardará la hora, el minuto y los segundos en el que empieza el programa.
inicio = time.time()

############################## Bucle while ##############################

# Creamos una variable i para que vaya sumando cada vez que pase por un número.
# Mientras i sea inferior al número:
# si el resto de i entre 2 es igual a 0, incluye el número dentro de la lista de pares y suma 1 a i
# si no, incluye el número dentro de la lista de impares y suma 1 a i

# i = 0
# while i < num:
#     if i % 2 == 0:
#         pares.append(i)
#         i += 1
#     else:
#         impares.append(i)
#         i += 1

############################## Bucle for ##############################

# Por cada i en el rango entre 0 y el número,
# si el resto de i entre 2 es igual a 0, incluye el número en la lista de pares
# si no, incluye el número en la lista de impares.


for i in range(num):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)


# Imprimimos los resultados
print(f"Los números pares son: {pares}")
print(f"Los números impares son: {impares} ")

# creamos la variable fin que guardará la hora, minutos y segundos exactos
fin = time.time()

# Imprimimos el tiempo de ejecución haciendo la resta del tiempo final y el inicial.
print("El tiempo de ejecución es ", fin - inicio)


# Pregunta: ¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente una 
# solución es más eficiente? Investiga para comprobarlo.

#Respuesta: Tras ejecutar el programa diversas veces con los dos bucles he llegado a la conclusión de que
# con tan pocas líneas de código no existe mucha diferencia entre un bucle y otro. Tal vez, teniendo
# un programa más elaborado y usando únicamente un solo tipo de bucle, es posible que encontráramos diferencias
# notables. Sin embargo, mi opinión reside en que tanto uno como otro tipo de bucles posee su función y 
# un programador debe reconocer el momento adecuado para utilizarlo.