# Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.

# 1. Definimos las funciones para calcular el área en un triángulo y en un cuadrado
def area_triangulo(base, altura):
    return (base*altura)/2


def area_cuadrado(altura):
    return altura**2


# 2. Pedimos al usuario que elija entre calcular un triángulo o un cuadrado mediante un número (1 o 2)
area = int(input(
    "¿Qué quieres calcular, un triángulo(1) o un cuadrado(2)? Introduce el número: "))

# 3. Si elige el número 1 (triángulo), se calculará según la función del área de un triángulo.
if area == 1:
    base = int(input("Introduce la base de tu triángulo: "))
    altura = int(input("Introduce la altura de tu triángulo: "))
    print("El área de tu triángulo es", area_triangulo(base, altura))

# 4. De otra manera, se calculará según la función del área de un cuadrado.
elif area == 2:
    altura = int(input("Introduce el área de tu cuadrado: "))
    print("El área de tu cuadrado es", area_cuadrado(altura))

else:
    print("Me temo que has introducido un número erróneo. Vuelve a inicializar el programa y elige entre 1 para triángulo o 2 para cuadrado.")
