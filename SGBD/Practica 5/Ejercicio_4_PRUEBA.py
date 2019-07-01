#!/usr/bin/python

# Imports necesarios
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#LEO EL CSV
data = pd.read_csv('dataset.csv')
print(data.head())
print(data.shape)

NS = data['NS']
MC = data['surface_total_in_m2']
CA = data['rooms']

def dot(v, w):
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


#beta = [beta0, beta1, beta2, beta3]
beta = [0, 1, 2, 3]

variables = [1, NS, MC, CA]

def predict(variables1, beta1):
	return dot(variables1, beta1)
	
def error(x_i, y_i, beta):
	return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
	return error(x_i, y_i, beta) ** 2

def squared_error_gradient(x_i, y_i, beta):
	return [-2 * x_ij * error(x_i, y_i, beta)for x_ij in x_i]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
	data = zip(x, y)
	theta = theta_0
	alpha = alpha_0
	min_theta, min_value = None, float("inf")
	iterations_with_no_improvement = 0
	while iterations_with_no_improvement < 100:
		value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )
		if value < min_value:
			min_theta, min_value = theta, value
			iterations_with_no_improvement = 0
			alpha = alpha_0
		else:
			iterations_with_no_improvement += 1
			alpha *= 0.9
		for x_i, y_i in in_random_order(data):
			gradient_i = gradient_fn(x_i, y_i, theta)
			theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
	return min_theta

def estimate_beta(x, y):
	beta_initial = [random.random() for x_i in x[0]]
	return minimize_stochastic(squared_error, squared_error_gradient, x, y, beta_initial, 0.001) 

#beta = estimate_beta(x, daily_minutes_good)
	

print(predict(variables,beta))
#plt.show()
