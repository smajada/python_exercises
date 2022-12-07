# Pida al usuario tres números y un cuarto número, y compruebe si este último es divisor de los tres números primeros.

# Pedimos al usuario tres números
print("Inserta tres números.")
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

# Pedimos al usuario otro número con el que comprobar que es divisor de los tres anteriores
print("Ahora inserta el número con el que quieres comprobar que es divisor de los tres anteriores.")
d = int(input("Cuarto número: "))

# Si d el resto de "d" es igual a 0 en cada uno de los casos, podemos decir que es divisor de ellos
if (a % d == 0) and (b % d == 0) and (c % d == 0):
    print("El último número es divisor de los tres primeros.")

# En caso contrario, no es divisor
else:
    print("El último número NO es divisor de los tres primeros.")
