#!/usr/bin/python

import numpy as np

def binomial(n, p):
	contadorExitos = 0 
	listaResultados = []
	for x in range (0, n):
		num =  np.random.rand()
		listaResultados.append(num)
	print (np.array(listaResultados))
	for j in range (0, n):
		if (listaResultados[j] < p):
			listaResultados[j] = 1
			contadorExitos += 1
		else:
			listaResultados[j] = 0
	print (np.array(listaResultados))
	print ("Se observan",contadorExitos,"exitos en",n, "repeticiones") 
binomial(15, 1/2)
		
	
