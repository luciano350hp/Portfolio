#!/usr/bin/python

import numpy as np
import Practica6_Ej2_1 as bernoulli

def hipergeometrica(r, b, k):
	contadorAzules = 0
	for j in range (0, k):
		pSacarAzul = b/(b+r)
		if (bernoulli.bernoulli(pSacarAzul)==1):
			b -= 1
			contadorAzules += 1
		else:
			r -= 1
	return contadorAzules
	
print(hipergeometrica(10, 7, 5)) 
