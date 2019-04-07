#!/usr/bin/python

import re
import collections

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

#	Hacer lista de 10 palabras mas usadas
listaPalabras = texto.split(' ')

listaOcurrenciasPalabras = collections.Counter(listaPalabras)

# print (listaOcurrenciasPalabras)

lista10palabras = []
lista10ocurrencias = []
# print the 10 most common words and their counts
for word, count in listaOcurrenciasPalabras.most_common(11):	#11 porq la primer palabra es ''
	lista10palabras.append(word)
	lista10ocurrencias.append(count)
	

lista10palabras.pop(0)			#elimino primer elemento ''
lista10ocurrencias.pop(0)

print (lista10palabras)
print (lista10ocurrencias)


#		HISTOGRAMA
xs = [i + 0.1 for i, _ in enumerate(lista10palabras)]

plt.bar(xs, lista10ocurrencias)
plt.ylabel("# Ocurrencias")
plt.title("Palabras")

plt.xticks([i + 0.5 for i, _ in enumerate(lista10palabras)], lista10palabras)
plt.show()






