# Escribe un programa que pida un número al usuario y escriba si primo o no

# Se define una función para calcular si un número es primo
def num_primo(num):
    # Los números primos se cuentan solo a partir del 2, por lo que cualquier número menor o igual a 1 no es primo
    if num <= 1:
        return False
    else:
        # Por cada número (i) que esté entre 2 y el número (num) que le demos
        for i in range(2,num):
            # Si el número (num) es divisible per alguno de los números (i) por los que pase
            if (num % i) == 0:
                # No es primo
                return False
            else:
            # En cualquier otro caso, sí que lo es
             return True

# Se inserta el número
num = int(input("Escribe un número: "))

# Si la función num_primo, a la que se le ha dado el valor del número insertado, es True, imprime que sí es un número primo
if num_primo(num) == True:
    print("El número aportado es primo")
    
# De otro modo, devuelve que NO es un número primo
else:
    print("El número aportado NO es primo")