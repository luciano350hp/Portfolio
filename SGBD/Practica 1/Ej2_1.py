#!/usr/bin/python

import re
import collections
from Funciones import textoSinPuntuacion
from Funciones import listaOcurrencias


# EJERCICIO 2
# EJERCICIO 2.1

textoV2 = ''
archivo = open("king_lear.txt", 'r')
texto1 = archivo.read()

#	PASAR PALABRAS A MINUSCULAS
texto1 = texto1.lower()

#	DESCARTAR SIGNOS DE PUNTUACION
textoV2 = textoSinPuntuacion(texto1)

textoV2 = textoV2.replace('\n',"")

#	SEPARAR Y CONTAR OCURRENCIAS DE LAS PALABRAS	-	ORDENAR DE MODO DESCENDENTE
listaPalabras = textoV2.split(' ')

listaOcurrenciasPalabras = listaOcurrencias(listaPalabras)

print (listaOcurrenciasPalabras)


#	CUANTAS PALABRAS TIENE EL TEXTO?	22735

print (len(listaPalabras))

#	LAS 5 MAS USADAS:

# 5 primeras de listaOcurrenciasPalabras
