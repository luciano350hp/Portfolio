#!/usr/bin/python

import numpy as np

def pascal(m, p):
	contadorExito = 0
	listaResultados = []
	num =  np.random.rand()
	while (contadorExito < m):
		while not (num < p):
			print(num)
			listaResultados.append(0)
			num =  np.random.rand()
		print(num)
		contadorExito += 1
		listaResultados.append(1)
		num =  np.random.rand()
	print(np.array(listaResultados)) 
	print ("Se repitió el experimento",len(listaResultados), "veces hasta obtener",m, "exitos")		
pascal(5, 1/2)
	
