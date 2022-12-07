# Sergio Majada Manresa
# 1º DAW

# Importamos la librería random
import random

# Creamos dos variables que guarden el valor mínimo y el máximo.
minimo = int(input("Valor mínimo: "))
maximo = int(input("Valor máximo: "))

# Mientras el máximo sea inferior al mínimo, indica que no es posible y cambiamos la variable máximo a un nuevo valor.
while maximo < minimo:
    maximo = int(
        input(f"{maximo} es menor que {minimo}. Vuelve a introducir un valor máximo: ")
    )

# Creamos una variable que guarde un número random.
num_random = random.randint(minimo, maximo)

# Iniciamos el programa con un mensaje.
print(f"Piensa un número entre {minimo} y {maximo}, a ver si lo puedo adivinar.")

# Creamos una variable de tipo string vacía que guarde las respuestas.
respuesta = ""

# Mientras la respuesta no sea "igual", pedimos una respuesta.
while respuesta != "igual":
    respuesta = input(f"Es {num_random}?: ")

# Si la resta del máximo y el mínimo es igual a uno y la respuesta no es igual, 
# estás haciendo trampas. Así que el programa ya no querrá jugar contigo.
    if maximo - minimo == 1 and respuesta != "igual":
        print(
            f"¡Has hecho trampas! Ya no quiero jugar contigo."
        )
        break

# Si la respuesta es mayor, se cambia la variable mínimo por el número random
# y se crea un nuevo número random entre el nuevo mínimo y el máximo.
    elif respuesta == "mayor":
        minimo = num_random
        num_random = random.randint(minimo, maximo)

# Si la respuesta es menor, se cambia la variable máximo por el número random
# y se crea un nuevo número random entre el nuevo máximo y el mínimo.
    elif respuesta == "menor":
        maximo = num_random
        num_random = random.randint(minimo, maximo)

# Una vez que se sale del bucle da las gracias.
print("¡Gracias por jugar!")
