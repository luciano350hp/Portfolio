#!/usr/bin/python

import re
import collections

textoV1 = ''
archivo = open("king_lear.txt", 'r')
lista = archivo.read()

#texto en minusculas
lista = lista.lower()


#texto en minusculas sin puntuacion
texto = re.findall(r'[^.,:;<>()¿?!]+', lista)
for palabra in texto:
		textoV1 = textoV1 + palabra
		
#texto sin \n
textoV1 = textoV1.replace('\n',' ')

#Armo lista de todas las palabras del texto
listaPalabras = textoV1.split(' ')

#Armo lista de ocurrencias
listaOcurrenciasPalabras = collections.Counter(listaPalabras)

print (listaOcurrenciasPalabras)
print ("******")
print (listaPalabras)
print ("******")
print (len(listaPalabras))

