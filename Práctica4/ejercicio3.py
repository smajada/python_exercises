# Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.

# Pide dos números
n1 = int(input("Escribe un número: "))
n2 = int(input("Escribe un número mayor que el anterior:"))

# Declaras una variable con valor 0 para que vaya sumando
sum = 0

# Por cada i en el rango n1, n2, suma = suma + i
for i in range(n1, n2):
    sum += i

# Imprime el último valor sum
print(sum)
