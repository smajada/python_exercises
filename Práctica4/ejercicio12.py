# Escribe un programa que pida un número y escriba si primo o no
# Dame un número: 123
# El número 123 no es primo
# Dame un número:127
# El número 127 es primo

# Se define una función para calcular si un número es primo
def num_primo(num):
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


# Se inserta el número
num = int(input("Escribe un número: "))

# Si la función num_primo, a la que se le ha dado el valor del número insertado, es True, imprime que sí es un número primo
if num_primo(num) == True:
    print(f"{num} es primo")

# De otro modo, imprime que NO es un número primo
else:
    print(f"{num} NO es primo")