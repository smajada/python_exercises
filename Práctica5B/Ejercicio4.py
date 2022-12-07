# Sergio Majada Manresa
# 1º DAW

# Importamos la librería random
import random

# Creamos tres variables: la que nos da el valor mínimo, el valor máximo y el secreto será el número a adivinar.
minimo = int(input("Valor mínimo:"))
maximo = int(input("Valor máximo:"))
secreto = random.randint(minimo, maximo)

# Inicializamos el programa.
print(f"A ver si adivinas un número entre {minimo} y {maximo}.")

# Pedimos un número y creamos una variable para ir contando los intentos.
num = int(input("Escribe un número: "))
intento = 1

# Mientras el numero insertado no sea igual que el nº random,
# Si el nº insertado es mayor que el nº random, avisa de que es más gande, pide otro nº y suma 1 al intento
# Si es menor, avisa de que es menor, pide otro nº y suma 1 al intento
while num != secreto:
    if num > secreto:
        num = int(input("¡Demasiado grande! Vuelve a probar: "))
        intento += 1
    else:
        num = int(input("¡Demasiado pequeño! Vuelve a probar: "))
        intento += 1

# Cuando el nº insertado y el nº random son iguales, imprime que es correcto y cuántas
# veces se ha intentado.
print(f"¡Correcto! Lo has intentado {intento} veces")
