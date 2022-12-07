# Sergio Majada Manresa
# 1º DAW

# Creamos dos variables: una lista y un nombre para empezar el programa.
lista = []
nombre = input("Dame un nombre: ")

# Mientras el nombre sea diferente a un Enter:
# Creamos una sublista, le insertamos el nombre y pedimos una nota.
while nombre != "":
    sublista = []
    sublista.append(nombre)
    nota = float(input("Escribe una nota: "))

# Mientras la nota sea superior a 0 e inferior a 10:
# Añadimos la nota a la sublista y volvemos a pedir otra nota.
    while (nota > 0) and (nota < 10):
        sublista.append(nota)
        nota = float(input("Escribe otra nota: "))

# Cuando la condición ya no se cumpla, añadimos la sublista a la lista principal
# Y pedimos otro nombre
    lista.append(sublista)
    nombre = input("Dame un nombre: ")

# Imprimimos las notas de los alumnos usando un print + un for
print("Las notas de los alumnos son: ")

# Creamos una variable para ir guardando las notas de nuestro for
notas_alumno = ""

# por cada una de las sublistas en lista, el nombre será el primer elemento de la sublista
# la primera nota será un string con el segundo elemento de la sublista
for i in lista:
    nombre = i[0]
    primera_nota = str(i[1])

# por cada elemento de la sublista, entre el tercer elemento (el segundo es la primera nota) y el final,
# las notas de los alumnos será un guion y la nota convertida en string
    for j in range(2, len(i)):
        notas_alumno += " - " + str(i[j])

# Imprimimos el nombre : la primera nota y la concatenación de las notas con un guion
# Por último, reinicializamos las notas de los alumnos
    print(nombre + ": " + primera_nota + notas_alumno)
    notas_alumno = ""