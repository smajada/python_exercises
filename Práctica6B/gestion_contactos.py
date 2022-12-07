#Sergio Majada Manresa
# 1º DAW

# Creamos tres variables: un diccionario que será donde incluyamos los datos,
# una variable entera para crear el índice de los contactos
# una última para marcar la opción del menú, que tendrá por defecto 0
contactos = {}
num_contact = 0
menu = 0

# definimos una variable para crear los contactos con dos parámetros: 
# el diccionario creado y la variable num_contact que nos sirve como índice
def anadir_contacto(contactos, num_contact):

    # creamos una nueva variable de tipo diccionario que contenga todos los campos que necesitamos 
    # y que se insertará en nuestro diccionario principal
    datos = {
        "nombre": str(input("Escribe un nombre: ")),
        "primer apellido": str(input("Escribe un primer apellido: ")),
        "segundo apellido": str(input("Escribe un segundo apellido: ")),
        "teléfono": int(input("Escribe un número de teléfono: ")),
        "mail": str(input("Escribe un mail: ")),
    }

    # añadimos un nuevo par de key y valor al diccionario siendo la key el num_contact y el valor el 
    # nuevo diccionario creado e imprimimos el mensaje
    contactos.update({num_contact: datos})
    print(f"Tu nuevo contacto con ID {num_contact} es {contactos.get(num_contact)}")


# Creamos una función que imprima todos los pares que tenemos en el diccionario
def consultar_contactos(contactos):
    print(contactos.items())

# Creamos una función en la que pedimos al usuario una ID (lo que antes hemos llamado también num_contact) 
# e imprimimos el valor de dicha key
def consultar_cont_key(contactos):
    ID = int(input("¿Qué contacto deseas consultar? Introduce su ID: "))
    print(contactos.get(ID))

# Creamos una función en la que pedimos, otra vez, 
# la key y borramos esa key
def eliminar_contacto(contactos):
    ID = int(input("¿Qué contacto quieres eliminar? Escribe su ID: "))
    contactos.pop(ID)

# Imprimimos un mensaje de bienvenida
print("Bienvenide a tu gestor de contactos.")

# Sergio Majada Manresa
# 1º DAW

# Creamos el menú a través de un while: 
# Mientras menu no sea igual a 5, imprimimos un mensaje para indicar las opciones al usuario.
# Por cada una de las opciones, se llama a una de las funciones anteriormente creadas
while menu != 5:
    menu = int(
        input(
            'Elige una opción entre 1: "añadir", 2: "consultar todos", 3: "consultar por ID ", 4: "eliminar" o 5: "Salir": '
        )
    )

    if menu == 1:
        anadir_contacto(contactos, num_contact)
        # para poder crear diferentes contactos, se debe sumar 1 al número de contacto anterior
        num_contact += 1
    elif menu == 2:
        consultar_contactos(contactos)
    elif menu == 3:
        consultar_cont_key(contactos)
    elif menu == 4:
        eliminar_contacto(contactos)
    # cuando sale, se imprime un mensaje de despedida
    elif menu == 5:
        print("Gracias por tu tiempo. ¡Hasta otra!")
    # si se elige otro número, el programa imprime un mensaje y vuelve a comenzar.
    else:
        print(
            "No te he entendido bien. ¿Puede que no hayas escrito correctamente lo que quieres hacer?"
        )