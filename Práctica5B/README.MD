# Ejercicios while y listas II

## Table of Content
- [Ejercicio 1](#ejercicio-1)
- [Ejercicio 2](#ejercicio-2)
- [Ejercicio 3](#ejercicio-3)
- [Ejercicio 4](#ejercicio-4)
- [ejercicio 6](#ejercicio-6)
- [ejercicio 6](#ejercicio-6-1)
- [ejercicio 7](#ejercicio-7)

# Ejercicio 1
Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.

Escribe límite: 50

Escribe un valor: 10

Escribe otro valor: 45

45 es demasiado grande. Escribe otro valor: 1

Escribe otro valor: 39

El límite a alcanzar es 50. La lista creada es: 10, 1, 39


# Ejercicio 2
Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.

Dame un nombre: Pepe González

Dame el teléfono: 971971971

Dame un nombre: Macarena Gómez

Dame el teléfono: 971999999

Dame un nombre: Pascual Ribot

Dame el teléfono: 666555444

Dame un nombre: S

**Los nombres y teléfonos de la agenda son:**

Pepe González: 971971971

Macarena Gómez: 971999999

Pasqual Ribot: 666555444


# Ejercicio 3
Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. 

***Nota***: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]

Dame un nombre: Héctor Quiroga

Escribe una nota: 4

Escribe otra nota: 8.5

Escribe otra nota: 12

Dame otro nombre: Inés Valls

Escribe una nota: 7.5

Escribe otra nota: 1

Escribe otra nota: 2

Escribe otra nota: -5

Dame otro nombre:

**Las notas de los alumnos son:**

Héctor Quiroga: 4.0 - 8.5

Inés Valls: 7.5 - 1.0 - 2.0

# Ejercicio 4
Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores.

 El programa va decidiendo si son demasiado grandes o pequeños. 

***Pista:***

    import random
    import time

    minimo = int (input ( "Valor mínimo:"))
    max = int (input ( "Valor máximo:"))
    secreto = random.randint (mínimo, máximo)

Valor mínimo: 0

Valor máximo: 100

A ver si adivinas un número entero entre 0 y 100.

Escribe un número: 20

Demasiado pequeño! Volver a probar: 30

Demasiado grande! Volver a probar: 27

Correcto! Lo has intentado 3 veces.

# ejercicio 6
Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.

Valor mínimo: 0

Valor máximo: 100

Piensa un número entre 0 y 100 a ver si lo puedo adivinar.

Es 50 ?: mayor

Es 75 ?: menor

Es 62 ?: menor


Es 56 ?: mayor

Es 59 ?: igual

Gracias por jugar!!

**Mejoras (opcionales):**

* Que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
* Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al decir "26" le decimos "menor", el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.

# ejercicio 6
Desarrolla de nuevo el ejercicio de la **práctica anterior de los números primos, con while.** Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.

# ejercicio 7 
Desarrolla un programa que tenga las siguientes características:
* Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
* Dicho problema resuélvelo con bucles for y while. 
* Justifica en el propio programa porque una opción es adecuada y la otra no.
* ¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente una solución es más eficiente? Investiga para comprobarlo.

