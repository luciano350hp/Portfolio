#!/usr/bin/python

import re

str = 'nombre1,apellido1,DNI1/nombre2,apellido2,DNI2/nombre3,apellido3,DNI3'
match = re.search(r'(\w+\d),(\w+\d)', str)
if match:
	print (match.group(1),'',match.group(2))
print ("******")


nombres = re.findall(r'(\w+\d),(\w+\d)', str)
for email in nombres:
	print (email[0],'',email[1])

print ("******")
