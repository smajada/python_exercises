# Sergio Majada Manresa
# 1º DAW

# Creamos tres variables: la que guardará el número que le demos, una variable switch que marcará si es primo o no
# y la variable i que irá aumentando por cada iteración y dividiéndose con el número.
num = int(input("Inserta un número: "))
apoyo = 0
i = 2

# Mientras i sea menor que el número, si el resto del nº entre i es 0, cambiará la variable switch a 1
# e imprimirá que el número NO es primo. Luego, aumentará en 1 la variable i para volver a empezar con otro número.
while i < num:
    if num % i == 0:
        apoyo = 1
        print(f"{num} NO es un número primo, porque se puede dividir por {i}")
    i += 1

# Si el switch no cambia cuando el bucle acaba, significa que el número sí es primo.
if apoyo == 0:
    print(f"{num} es un número primo.")

# ____________________________________________________________

# Ambas opciones me parecen igual de validas. La mayor diferencia podría darse
# a la hora de la creación de variables, puesto que en la iteración while se necesita
# no solo crear la variable i, sino también una variable que cambie dependiendo de si
# la condición se cumple. 
# En cambio, en la iteración for, la creación de variables es innecesaria y, por decirlo 
# de alguna manera, el programa es más independiente. 
# Además, puesto que podríamos considerar este tipo de iteración como pautada entre 2 
# y el número que deseamos, una iteración for parece más conveniente que una iteración while. 