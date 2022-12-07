#Sergio Majada Manresa
#1º DAW

# Creamos dos variables que pedirán los números al usuario
num = int(input("Escribe un número: "))
mayor_num = int(input(f"Escribe un número mayor que {num}: "))

# Mientras la segunda variable sea igual o menor que el primer número,
# Se pedirá un nuevo input al usuario que se almacenará en una nueva variable (nuevo_num).
# Luego, la segunda variable (mayor_num) cambiará su valor al introducido en la nueva variable (nuevo_num)
while mayor_num <= num:
    nuevo_num = int(
        input(f"{mayor_num} no es mayor que {num}. Vuelve a introducir un número: ")
    )
    mayor_num = nuevo_num

# Cuando la condición ya no se cumpla, saldrá del bucle e imprimirá los dos números introducidos.
print(f"Los números que has escrito son {num} y {mayor_num}")
