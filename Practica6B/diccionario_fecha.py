def diccionario_fecha(num_fecha):  # definimos el procedimiento
    # creamos una varibale que contenga un diccionario con el número como llave 
    # y el nombre del mes como valor
    meses = {
        "01": "enero",
        "02": "febrero",
        "03": "marzo",
        "04": "abril",
        "05": "mayo",
        "06": "junio",
        "07": "julio",
        "08": "agosto",
        "09": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre",
    }

    # creamos una variable para contener la fecha en letras y dividimos la variable num_fecha a partir de los /
    # imprimimos el valor 0 de la string + "de" + cogemos el valor de la key al que se refiera el número que pongamos
    # + de + el año
    num_split = num_fecha.split("/")
    print(num_split[0] + " de " + meses.get(num_split[1]) + " de " + num_split[2])


# definimos la variable que acogerá la fecha en números y llamamos a la función
num_fecha = str(input("Introduce una fecha en formato dd/mm/aaaa: "))
diccionario_fecha(num_fecha)