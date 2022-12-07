# Sergio Majada Manresa
# 1º DAW

# Definimos la función que coja como parámetro una frase
def numero_palabras_blank(frase):
    palabras = (
        frase.split()
    )  # Dividimos la frase en palabras y las almacenamos en una variable
    print(len(palabras))  # Imprimimos el tamaño de la variable

def numero_palabras_strange(frase):
    

frase = str(input("Escribe una frase: "))
numero_palabras_blank(frase)  # Llamamos a la función
