#!/usr/bin/python

import numpy as np
import Practica6_Ej2_1 as bernoulli

def binomial(n, p):
	contadorExitos = 0 
	for x in range (0, n):
		contadorExitos += bernoulli.bernoulli(p)
	print ("Se observan",contadorExitos,"exitos en",n, "repeticiones")
	return contadorExitos 
binomial(15, 1/2)
		
	
