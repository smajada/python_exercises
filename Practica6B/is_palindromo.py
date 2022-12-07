# Sergio Majada Manresa
# 1º DAW

# Definimos una función que coge como parámetro una frase
def is_palindromo(frase):
    frase = frase.replace(" ", "")  # eliminamos los espacio de la frase
    i = 0  # indicamos el valor inicial de i
    isValid = True  # creamos una variable que nos indica si es válido o no, con valor True por defecto

    # Mientras i sea menor a la mitad de los carácteres de la frase y sea válida
    while i < len(frase) / 2 and isValid:
        if (
            frase[i] == frase[-(i + 1)]
        ):  # si el carácter con valor i y su contrario son iguales,
            i += 1  # sigue recorriendo la lista
        else:
            isValid = False  # si no, indica que isValid es falso
    return isValid  # cuando finalice, devuelve el valor de isValid


frase = str(input("Escribe una frase: "))  # Escribimos una frase

# Escribimos el resultado dependiendo de si la función es True o False
if is_palindromo(frase):
    print("Es palíndromo")
else:
    print("La frase NO es palíndroma")
