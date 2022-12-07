# Pida al usuario un importe en euros y diga si el cajero automático le 	
# puede dar dicho importe utilizando el mismo billete y el más grande
# (recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 €). 

#1. Leer el importe
importe = int(input("Introduzca un importe: "))

# Si el importe es menor de 500, 
if importe >= 500:
    # n_billetes ahora es el importe dividido (con número entero) por 500
    n_billetes = importe // 500
    # La división da como resultado el número de billetes de 500 que recibe
    print(f"Recibes {n_billetes} billetes de 500")
    # El importe ahora se transforma en el resto de dividir el importe por 500
    importe = importe % 500

# El resto de la división anterior, si es menor de 200, realiza la misma operación que la anterior.
# Así, hasta llegar a billetes de 5

if importe >= 200:
    n_billetes = importe // 200
    print(f"Recibes {n_billetes} billetes de 200")
    importe = importe % 200

if importe >= 100:
    n_billetes = importe // 100
    print(f"Recibes {n_billetes} billetes de 100")
    importe = importe % 100

if importe >= 50:
    n_billetes = importe // 50
    print(f"Recibes {n_billetes} billetes de 50")
    importe = importe % 50

if importe >= 20:
    n_billetes = importe // 20
    print(f"Recibes {n_billetes} billetes de 20")
    importe = importe % 20

if importe >= 10:
    n_billetes = importe // 10
    print(f"Recibes {n_billetes} billetes de 10")
    importe = importe % 10

if importe >= 5:
    n_billetes = importe // 5
    print(f"Recibes {n_billetes} billetes de 5")
    importe = importe % 5