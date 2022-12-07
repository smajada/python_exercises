# Sergio Majada Manresa
# 1º DAW

# Definimos una función que coja como parámetros una frase y una vocal
# Dentro de la función, definimos una variable que contenga las vocales
# Por cada una de las vocales contenidas en la variable, cambiamos la variable "frase"
# La varibale "frase" cambia la i (de la variable vocales) por la vocal que hemos puesto
# Cuando el bucle acaba, devuelve la variable frase
def vocales(frase, vocal):
    conjunto_vocales = "AEIOUaeiou"

    for i in conjunto_vocales:
        frase = frase.replace(i, vocal)
    return frase

# Introducimos las variables e imprimimos la función
frase = str(input("Introduce una frase: "))
vocal = str(input("Introduce una vocal: "))

print(vocales(frase, vocal))

# fraseUsuario = input("Escribe una frase: ")
# vocalUsuario = input("Escribe una vocal para sustituir en la frase anterior: ")
# def cambio_vocal(frase,vocal):
#     vocales = "aeiouAEIOU"
#     lista = []
#     for letra in frase:
#         if letra in vocales:
#             lista.append(vocalUsuario)
#         else :
#             lista.append(letra)
#         cambio = "".join(lista)
#     return cambio
# print(cambio_vocal(fraseUsuario,vocalUsuario))
