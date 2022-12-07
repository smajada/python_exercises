# Sergio Majada Manresa
# 1º DAW

import time

def for_primo(num):
    # Los números primos se cuentan solo a partir del 2
    if num > 1:
        # Por cada número (i) que esté entre 2 y el número (num) que le demos
        for i in range(2, num):
            # Si el número (num) es divisible por alguno de los números (i) por los que pase
            if (num % i) == 0:
                # No es primo
                return False
        # De otra forma, sí que es primo
        return True
    # Si el número es menor o igual a 1, no es primo
    else:
        return False


def while_primo(num):
    # Creamos dos variables: una variable switch que marcará si es primo o no
    # y la variable i que irá aumentando por cada iteración y dividiéndose con el número.
    is_primo = True
    i = 2

    # Mientras i sea menor que el número, si el resto del nº entre i es 0, cambiará la variable switch a 1
    # e imprimirá que el número NO es primo. Luego, aumentará en 1 la variable i para volver a empezar con otro número.
    while i < num:
        if num % i == 0:
            is_primo = False
        i += 1
    return is_primo

#Creamos tres variables: la pregunta que haremos, el número que deseamos saber si es primo 
# y una variable booleana para indicar si es primo o no, teniendo por predeterminado False
pregunta = str(input("Indica con qué deseas calcular el número primo (for o while): "))
num = int(input("Inserta un número: "))
is_primo = False

# Si responde con la respuesta elegida, inicia el contador de tiempo, 
# la función retorna un booleano, que cambia la variable is_primo
# finaliza el contador de tiempo y se imprime el resultado
if pregunta == "while":
    inicio = time.time()
    is_primo = while_primo(num)
    fin = time.time()
    if is_primo:
        print(f"El num {num} SÍ es primo")

    else:
        print(f"El número {num} NO es primo")

    print("El tiempo de ejecución es ", fin - inicio)

elif pregunta == "for":
    inicio = time.time()
    is_primo = for_primo(num)
    fin = time.time()
    if is_primo:
        print(f"El num {num} SÍ es primo")

    else:
        print(f"El número {num} NO es primo")

    print("El tiempo de ejecución es ", fin - inicio)

# Si la respuesta no es ninguna de las opciones, imprime un mensaje y termina el programa
else:
    print("No has escrito 'for' o 'while'. Tendrás que volver a iniciar el programa. ")
