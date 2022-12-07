# Escribe un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
# A continuación, debe mostrar todas las notas,  la nota media,
# la nota más alta que ha sacado así como también la menor nota que ha sacado

# Se define una función para declarar la nota máxima
def nota_maxima(tam_notas):
    # .sort() ordena el vector de menor a mayor
    tam_notas.sort()
    # La función imprime el mensaje cogiendo el último elemento del vector sea del tamaño que sea (-1)
    return print("La nota máxima es ", float(tam_notas[-1]))

# Se define otra función para declarar la nota máxima de la misma forma que la función anterior
def nota_minima(tam_notas):
    tam_notas.sort()
    # La función imprime el mensaje cogiendo el primer elemento del vector (0)
    return print("La nota mínima es ", float(tam_notas[0]))

# Se define otra función para declarar la nota media
def nota_media(tam_notas):
    #La variable media se calula a partir de la función sum(), que suma los elementos del vector y lo divide por el número total de 
    # ítems, calculado a partir de len()
    media = sum(tam_notas)/len(tam_notas)
    # Se imprime la variable media 
    return print("La nota media es: ", media)

# Se define la variable tam_notas como un vector
tam_notas = []

# Mientras el tamaño del vector sea menor que 5
while len(tam_notas) < 5:
    # Se inserta una nota
    nota = float(input("Inserta una nota: "))
    # Si la nota es igual o mayor que 0 y es menor o igual que 10
    if nota >= 0 and nota <= 10:
        # Se añade la nota
        tam_notas.append(nota)
        # Imprimir el vector, la nota máxima y la nota mínima
        print(tam_notas)
        nota_maxima(tam_notas)
        nota_minima(tam_notas)

    # Si no, imprimir un mensaje de error y seguir con el bucle
    else:
        print("La nota no puede ser inferior a 0 o superior a 10. Vuelve a insertar un número.")

# Cuando el bucle acabe, imprimir el vector, la nota máxima, la mínima y la media
print(tam_notas)
nota_maxima(tam_notas)
nota_minima(tam_notas)
nota_media(tam_notas)