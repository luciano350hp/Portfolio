#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def exponencial(lambdaa):
	num = np.random.rand()
	num = -(1/lambdaa) * (np.log(1-num))
	return num


	
