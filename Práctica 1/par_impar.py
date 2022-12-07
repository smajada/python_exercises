# Definir una función que defina un número par, es decir, aquel que siendo dividido entre 2 de como resto 0
def resto(N):
    return N % 2


# Leer número
N = int(input("Por favor, escribe un número: "))

# Si Resto de N es igual a 0
if resto(N) == 0:

    # Imprimir "¡Tu número SÍ es un número par!"
    print("¡Tu número SÍ es un número par!")

    # Sino
else:
    # Imprimir "Tu número NO es un número par!"
    print("¡Tu número NO es un número par!")

