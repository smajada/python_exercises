# Definir función para calcular el área del triángulo
def area_triangulo(base, altura):
    return int((base * altura) / 2)


# Leer base y altura
b = int(input("Introduce la base de tu triángulo: "))
h = int(input("Introduce la altura de tu triángulo: "))

# Imprimir área del triángulo
print("El área de tu triángulo es", area_triangulo(base=b, altura=h))
