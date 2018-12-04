#!/usr/bin/python

import numpy as np
import Practica6_Ej2_2 as geometrica

def pascal(m, p):
	contadork = 0
	for i in range(m):
		contadork += geometrica.geometrica(p)
	print ("Se repitió el experimento",contadork, "veces hasta obtener",m, "exitos")
	return contadork
pascal(5, 1/2)
	
