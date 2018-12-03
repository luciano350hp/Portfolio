#!/usr/bin/python

import numpy as np

def geometrica(p):
	contadork = 0
	num =  np.random.rand()
	while not (num < p):
		print(num)
		contadork += 1
		num =  np.random.rand()
	print(num)
	contadork += 1
	return contadork


