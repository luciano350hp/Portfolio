#!/usr/bin/python


# EJERCICIO 1
# EJERCICIO 1.2


import re

str = 'nombre1,apellido1,DNI1/nombre2,apellido2,DNI2/nombre3,apellido3,DNI3'

print ("cadena: "+str)
print ("")

nombres = re.findall(r'(\w+\d),(\w+\d)', str)
for nombre in nombres:
	print (nombre[0],'',nombre[1])
