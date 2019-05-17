#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import collections
import random
from Funciones import textoSinPalabrasProhibidas
from Funciones import listaOcurrencias

import matplotlib.pyplot as plt

archivo = open("king_lear.txt", 'r')
archivo2 = open("prohibidas.txt", 'r')
textoV1 = archivo.read()
listaProhibidas1 = archivo2.readlines()

#	ELIMINO DEL TEXTO LAS PALABRAS PROHIBIDAS 
texto, listaProhibidas = textoSinPalabrasProhibidas(textoV1,listaProhibidas1)

#	SEPARAR Y CONTAR OCURRENCIAS DE LAS PALABRAS	-	ORDENAR DE MODO DESCENDENTE
listaPalabras = texto.split(' ')
listaOcurrenciasPalabras = listaOcurrencias(listaPalabras)

listaOcurrenciasPalabras2 = listaOcurrenciasPalabras.most_common(50)

#Elimino el espacio vacio
listaOcurrenciasPalabras2.pop(0) 
print (listaOcurrenciasPalabras2)


def text_size(total):
	#equals 8 if total is 0, 28 if total is 200
	return 8 + total / 200 * 20

for palabra, ocurrencia in listaOcurrenciasPalabras2:
	plt.text(random.randint(0, 1000),random.randint(0, 1000), palabra,ha='center', va='center',size=text_size(ocurrencia))

plt.xlabel("50 PALABRAS MAS REPRESENTATIVAS")
plt.axis([0, 1000, 0, 1000])
plt.xticks([])
plt.yticks([])
plt.show()

