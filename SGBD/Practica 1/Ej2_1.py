#!/usr/bin/python
# -*- coding: utf-8 -*-

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

# 	REEMPLAZAR - CON ESPACIO
textoV2 = textoV2.replace('-',' ')

#	SEPARAR Y CONTAR OCURRENCIAS DE LAS PALABRAS	-	ORDENAR DE MODO DESCENDENTE
texto = ""
for palabra in textoV2.split():
	texto += " " + palabra + " "

print (texto)

listaOcurrenciasPalabras = listaOcurrencias(texto.split())

print (listaOcurrenciasPalabras)


#	CUANTAS PALABRAS TIENE EL TEXTO?	22735

print (len(texto))

#	LAS 5 MAS USADAS:

# 5 primeras de listaOcurrenciasPalabras
