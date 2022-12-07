#Sergio Majada Manresa
#1º DAW

# Creamos dos variables: una para la inserción de los números y la otra será nuestra lista.
# La variable n_notas debe ser un float para que permita decimales.
n_nota = float(input('Escribe una nota: '))
notas = []

# mientras la variable n_nota sea mayor o igual a 0 y menor o igual a 10,
# insertaremos la nota en la lista creada y pediremos otro número.
while (n_nota >= 0) and (n_nota <= 10):
    notas.append(n_nota)
    n_nota = float(input('Escribe una nota: '))

#Cuando la condición no se cumpla, impriremos la lista
print(f"Las notas que has escrito son {notas}")