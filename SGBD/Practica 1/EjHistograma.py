#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import collections
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

#Lista 10 Palabras y su cantidad de ocurrencias
lista10palabras = []
lista10ocurrencias = []

# TOMO LAS PRIMERAS 10 PALABRAS
for word, count in listaOcurrenciasPalabras.most_common(10):	
	lista10palabras.append(word)
	lista10ocurrencias.append(count)

print (listaOcurrenciasPalabras)
print (lista10palabras)
print (lista10ocurrencias)

lista10ocurrencias.pop(0)
lista10palabras.pop(0)

#		HISTOGRAMA
xs = [i + 0.1 for i, _ in enumerate(lista10palabras)]

plt.bar(xs, lista10ocurrencias)
plt.ylabel("# Ocurrencias")
plt.title("Palabras")

plt.xticks([i + 0.5 for i, _ in enumerate(lista10palabras)], lista10palabras)
plt.show()
