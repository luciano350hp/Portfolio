#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def bernouli(p):
	num =  np.random.rand()
	print(num)
	if (num < p):
		return 1
	else:
		return 0
print(bernouli(1/2)) 
		
	
