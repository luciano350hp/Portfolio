#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def exponencial(lambdaa):
	num = np.random.rand()
	num = -(1/lambdaa) * (np.log(1-num))
	return num

def poisson(lambdaa):
	tiempo = 0
	contador = 0
	while(tiempo <= 1):
		num = exponencial(lambdaa)
		tiempo += num
		contador += 1
	return contador

def grafico(lambdaa):
	listaPoisson = []
	cantidadPoisson = 4000
	for i in range(0, cantidadPoisson):
		listaPoisson.append(poisson(lambdaa))
	plt.hist(listaPoisson,50)
	plt.show()

grafico(12)	

	
