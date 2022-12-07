# Sergio Majada Manresa
# 1º DAW

# Introducimos tres variables que intruduzcan el nombre y los apellidos.
nombre = str(input('Escribe un nombre: '))
primer_apellido = str(input('Escribe el primer apellido: '))
segundo_apellido = str(input('Escribe el segundo apellido: '))

# Creamos una función que pase como parámetros las tres variables creadas.
# Creamos una variable "lista" en la que se introduzcan las tres variables,
# Creamos otra variable introduciendo un espacio vacío
# De esta función devolveremos, en forma de cadena, los tres parámetros separados por un espacio.
def nombre_y_apellido(nombre, primer_apellido, segundo_apellido):
    lista = [nombre, primer_apellido, segundo_apellido]
    return " ".join(lista)

# Imprimimos la función
print(nombre_y_apellido(nombre, primer_apellido, segundo_apellido))