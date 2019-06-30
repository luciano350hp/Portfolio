#!/usr/bin/python
# -*- coding: utf-8 -*-

#PRACTICA 4 EJERCICIO 4-3		--	Usando Funciones para nube de palabras de Práctica 1

import collections
import random
#from Funciones import textoSinPalabrasProhibidas
from Funciones import listaOcurrencias

import matplotlib.pyplot as plt

import re
import psycopg2
import sys
import pymongo
from pprint import pprint

conn = pymongo.MongoClient()
db = conn.test
col = db.tweets

con = None

#	Todos los textos de Venezuela
VeneTexts = list(col.find({'countryCode':'VEN'},{'text':'1', '_id':False}))
#	Todos los textos de Argentina
ArgTexts = list(col.find({'countryCode':'ARG'},{'text':'1', '_id':False}))
	
#	Concatenamos todos los textos en un solo string para despues contar las palabras del resultado total
VeneText = ''
for text in VeneTexts:
	VeneText = VeneText + ' ' + str(text['text'])


ArgText = ''
for text in ArgTexts:
	ArgText = ArgText + ' ' + str(text['text'])

#print ('Textos Vene')
#print (VeneText)
	
	
#--------------------------------------------------------------------------------------------------------
#		NUBE PALABRAS VENEZUELA

# #	SEPARAR Y CONTAR OCURRENCIAS DE LAS PALABRAS
listaPalabrasVene = VeneText.split(' ')
listaOcurrenciasPalabras = listaOcurrencias(listaPalabrasVene)			# Esta funcion listaOcurrencias() esta implementada en el archivo Funciones

listaOcurrenciasPalabrasVene = listaOcurrenciasPalabras.most_common(20)

#Elimino el espacio vacio
listaOcurrenciasPalabrasVene.pop(0) 
print (listaOcurrenciasPalabrasVene)


def text_size(total):
	#equals 8 if total is 0, 28 if total is 200
	return 8 + total / 200 * 20

for palabra, ocurrencia in listaOcurrenciasPalabrasVene:
	plt.text(random.randint(0, 1000),random.randint(0, 1000), palabra,ha='center', va='center',size=text_size(ocurrencia))

plt.xlabel("20 PALABRAS MAS REPRESENTATIVAS")
plt.axis([0, 1000, 0, 1000])
plt.xticks([])
plt.yticks([])
plt.show()



#--------------------------------------------------------------------------------------------------------
#		NUBE PALABRAS ARG

# #	SEPARAR Y CONTAR OCURRENCIAS DE LAS PALABRAS
listaPalabrasArg = ArgText.split(' ')
listaOcurrenciasPalabras2 = listaOcurrencias(listaPalabrasArg)

listaOcurrenciasPalabrasArg = listaOcurrenciasPalabras2.most_common(20)

#Elimino el espacio vacio
listaOcurrenciasPalabrasArg.pop(0) 
print (listaOcurrenciasPalabrasArg)


def text_size(total):
	#equals 8 if total is 0, 28 if total is 200
	return 8 + total / 200 * 20

for palabra, ocurrencia in listaOcurrenciasPalabrasArg:
	plt.text(random.randint(0, 1000),random.randint(0, 1000), palabra,ha='center', va='center',size=text_size(ocurrencia))

plt.xlabel("20 PALABRAS MAS REPRESENTATIVAS")
plt.axis([0, 1000, 0, 1000])
plt.xticks([])
plt.yticks([])
plt.show()


