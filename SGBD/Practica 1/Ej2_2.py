#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import collections
from Funciones import *

# EJERCICIO 2
# EJERCICIO 2.2	
#	PALABRAS PROHIBIDAS

archivo = open("king_lear.txt", 'r')
archivo2 = open("prohibidas.txt", 'r')
textoV1 = archivo.read()
listaProhibidas = archivo2.readlines()

print ('------------------------------')
print(textoV1)
print ('*********')
texto, listaProhibidas = textoSinPalabrasProhibidas(textoV1,listaProhibidas)
print ("Prohibidas:", listaProhibidas)
print ('*********')
print (texto)

