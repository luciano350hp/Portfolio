#!/usr/bin/python

import numpy as np

def geometrica(p):
	contadork = 0
	listaResultados = []
	num =  np.random.rand()
	while not (num < p):
		print(num)
		contadork += 1
		listaResultados.append(0)
		num =  np.random.rand()
	print(num)
	contadork += 1
	listaResultados.append(1)
	print(np.array(listaResultados)) 
	print ("Se repitió el experimento",contadork, "veces")		
geometrica(1/2)
