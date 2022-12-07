# Sergio Majada Manresa
# 1º DAW

# Creamos una variable en la que introduzcamos una frase
frase = str(input("Escribe una frase: "))

# definimos el procedimiento, en el que se incluye como parámetro la frase anterior
# por cada carácter en la frase,
# imprimimos el carácter
def caracter(frase):
    for i in frase:
        print(i)


# llamamos al procedimiento
caracter(frase)
