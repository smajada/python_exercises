# Sergio Majada Manresa
# 1º DAW

#Definimos una función que sustituye el espacio en blanco por un asterisco
def asterisco(frase):
   return frase.replace(" ", "*")     


def asterisco2(frase):
   frase_nueva= ""
   for i in frase:
      if i == " ":
         i = "*"
      frase_nueva += i
   return frase_nueva

# Insertamos una frase e imprimimos la función
frase = str(input('Escribe una frase: '))
print(asterisco(frase))