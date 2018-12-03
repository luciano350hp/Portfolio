#!/usr/bin/python

import numpy as np
import Practica6_Ej2_2 as geometrica

def pascal(m, p):
	contadorExito = 0
	contadork = 0
	while (contadorExito < m):
		contadork += geometrica.geometrica(p)
		contadorExito += 1
	print ("Se repitió el experimento",contadork, "veces hasta obtener",m, "exitos")
	return contadork
pascal(5, 1/2)
	
