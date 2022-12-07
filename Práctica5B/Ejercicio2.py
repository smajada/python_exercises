# Sergio Majada Manresa
# 1º DAW

# Creamos dos variables: la agenda, que será una lista y un nombre, para empezar el programa.
agenda = []
nombre = str(input("Dame un nombre: "))

# Mientras el nombre sea diferente a S, se pide el teléfono, se añaden ambos elementos a la lista y se vuelve a
# pedir un nombre.
while nombre != "S":
    telefono = int(input("Dame un teléfono: "))
    agenda.append([nombre, telefono])
    nombre = str(input("Dame un nombre: "))

# Cuando se cumple la condición, se imprime la agenda
print("Los nombres y teléfonos de la agenda son:")

# Por cada sublista (i) que hay en nuestra agenda (marcado con su len)
# Se imprime el elemento 0 (siempre será el nombre), ": " y el elemento 1 (siempre el nº)
for i in range(len(agenda)):
    print(agenda[i][0] + ": " + str(agenda[i][1]))
