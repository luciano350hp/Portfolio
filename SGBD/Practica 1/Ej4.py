#!/usr/bin/python

import re
import collections

#1er intento...
textoV1 = ''
archivo = open("king_lear.txt", 'r')
lista = archivo.read()
lista = lista.lower()
#lista = lista.strip()


texto = re.findall(r'[^.,:;<>()¿?!]+', lista)
for palabra in texto:
		textoV1 = textoV1 + palabra
		
#print (textoV1)	#texto en minusculas sin puntuacion

textoV1 = textoV1.replace('\n',' ')

#print (textoV1)

listaPalabras = textoV1.split(' ')

listaOcurrenciasPalabras = collections.Counter(listaPalabras)

print (listaOcurrenciasPalabras)
print (listaPalabras)
print (len(listaPalabras))

