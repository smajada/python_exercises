# Escribe un programa que pida un número e imprima todos sus divisores.
# Dame un número: 200
# Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200

# Creamos una variable que pedirá al usuario un número
num = int(input('Escribe un número: '))

# por cada número entre 1 y el número + 1 (porque si no indicamos el +1, el bucle solo llega hasta un número anterior al indicado)
for i in range(1, num+1):
    # Si el resto de la división entre el número e i es igual a 0
    if num % i == 0:
        # Imprime este número, que será el divisor del número indicado en la variable
        print (i, end=' ')