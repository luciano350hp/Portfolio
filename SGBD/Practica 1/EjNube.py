#!/usr/bin/python

import re
import collections
import random

#import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import animation


textoV1 = ''
archivo = open("king_lear.txt", 'r')
archivo2 = open("prohibidas.txt", 'r')
texto = archivo.read()
texto = texto.lower() #minusculas
lista2 = archivo2.readlines()	#leo lineas del archivo de prohibidas y armo array
lista2 = list(map(lambda x: x.strip() , lista2)) #Quito el '/n' de la lista de prohibidas
texto = texto.replace('\n',' ')	#elimino los \n del texto

#print (lista2)	#lista de prohibidas
#print (texto)

for palabra in lista2:
		texto = texto.replace(palabra,'')	# reemplazo cada palabra prohibida en el texto


#print (texto)

#	Hasta aca tenemos el texto en minusculas sin las palabras prohibidas

#	Hacer lista de 50 palabras mas usadas
listaPalabras = texto.split(' ')

listaOcurrenciasPalabras = collections.Counter(listaPalabras)

listaOcurrenciasPalabras2 = listaOcurrenciasPalabras.most_common(50)

print (listaOcurrenciasPalabras2)




def text_size(total):
	#equals 8 if total is 0, 28 if total is 200
	return 8 + total / 200 * 20

for palabra, ocurrencia in listaOcurrenciasPalabras2:
	plt.text(random.randint(0, 1000),random.randint(0, 1000), palabra,ha='center', va='center',size=text_size(ocurrencia))

plt.xlabel("Popularity on Job Postings")
plt.ylabel("Popularity on Resumes")
plt.axis([0, 1000, 0, 1000])
plt.xticks([])
plt.yticks([])
plt.show()

