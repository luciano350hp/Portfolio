#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def exponencial(lambdaa):
	listaRandom = []
	cantidadRandom = 4000
	for i in range(0, cantidadRandom):
		listaRandom.append(np.random.rand())
	print("La lista random es \n",np.array(listaRandom))
	listaExponencial = list(map(lambda y: -(1/lambdaa) * (np.log(1-y)), listaRandom))
	print("La lista exponencial es \n",np.array(listaExponencial))
	plt.hist(listaExponencial,50)
	plt.show()	
exponencial(1)
	
