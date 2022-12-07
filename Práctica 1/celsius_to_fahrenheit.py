# Definir función de conversión
def celsius_to_fahrenheit(grados_celsius):
    return grados_celsius * (9 / 5) + 32


# Leer grados centígrados (puede contener decimales)
grados_celsius = float(input("Por favor, introduce los grados centígrados: "))

# Imprimir: los grados celsius introducidos + string + la conversión a grados fahrenheit + string.
print(
    grados_celsius,
    " grados Celsius son",
    celsius_to_fahrenheit(grados_celsius),
    "grados Fahrenheit",
)
