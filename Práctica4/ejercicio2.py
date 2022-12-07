# Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares

# Insertar los números
n1 = int(input('Escribe un número: '))
n2 = int(input('Escribe un número mayor que el anterior:'))

if n1 > n2:
    print ('Error')
else:
    # Por cada número (i) entre n1 y n2, si i es par, imprime que es par. Si no, imprime que no lo es.
    for i in range(n1, n2):
        # Si el resto de i entre 2 es igual a 0, imprime que es par
        if i%2 == 0:
            print('El número', i, 'es par')
        # Si no, imprime que es impar.
        else:
            print('El número', i, 'es impar')        
