#!/usr/bin/python

import numpy as np
import Practica6_Ej3 as exponencial
import matplotlib.pyplot as plt

def poisson(lambdaa):
	tiempo = 0
	contador = 0
	while(tiempo <= 1):
		num = exponencial.exponencial(lambdaa)
		tiempo += num
		contador += 1
	return contador


	
