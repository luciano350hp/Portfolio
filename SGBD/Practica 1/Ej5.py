#!/usr/bin/python

import re
import collections

#1er intento...
textoV1 = ''
archivo = open("king_lear.txt", 'r')
archivo2 = open("prohibidas.txt", 'r')
texto = archivo.read()
texto = texto.lower()
lista2 = archivo2.readlines()
lista2 = list(map(lambda x: x.strip() , lista2)) #Quito el '/n'.

print (lista2)
#print (texto)

for palabra in lista2:
		texto = texto.replace(palabra,'')

print ('*********')
print (texto)
