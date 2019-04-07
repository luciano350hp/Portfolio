#!/usr/bin/python

import re
import collections

textoV1 = ''
archivo = open("king_lear.txt", 'r')
archivo2 = open("prohibidas.txt", 'r')
texto = archivo.read()
texto = texto.lower()
listaProhibidas = archivo2.readlines()
listaProhibidas = list(map(lambda x: x.strip() , listaProhibidas)) #Quito el '/n'.

for palabra in listaProhibidas:
		texto = texto.replace(palabra,'')

print (listaProhibidas)
print ('*********')
print (texto)
