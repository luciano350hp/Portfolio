#!/usr/bin/python

import numpy as np
from random import shuffle

def hipergeometrica(r, b, k):
	listaBolitas = []
	for j in range (0, r): #Pongo las bolitas rojas en la bolsa
		listaBolitas.append('red')
	for i in range (0, b): #Pongo las bolitas azules en la bolsa
		listaBolitas.append('blue')
	shuffle(listaBolitas) #Las mezclo de forma random
	print("Las bolitas en la bolsa son: ",np.array(listaBolitas))
	listaBolitask = np.random.choice(listaBolitas, k, replace=False)
	print("Se tomaron",k,"bolitas: ", listaBolitask)
	listaRojas = list(filter(lambda x: (x == 'red') , listaBolitask))
	print("De esa muestra hay",len(listaRojas),"bolitas rojas")
hipergeometrica(10, 7, 5) 
		
	
