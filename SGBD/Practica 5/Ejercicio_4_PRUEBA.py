#!/usr/bin/python

# Imports necesarios
import numpy as np
import pandas as pd
import math
import random

#LEO EL CSV
data = pd.read_csv('dataset.csv')

NS = data['NS']
MC = data['surface_total_in_m2']
CA = data['rooms']
VP = data['price']


l = len(NS)

x = []
y = []

for i in range (0, l):
	x1 = [1, int(NS[i]),int(MC[i]),int(CA[i])]
	x.append(x1)
	y.append(int(VP[i]))

def dot(v, w):
	return sum(v_i * w_i for v_i, w_i in zip(v, w))

def predict(variables1, beta1):
	return dot(variables1, beta1)
	
def error(x_i, y_i, beta):
	return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
	return error(x_i, y_i, beta) ** 2

def sum_of_squared_errors(alpha, beta, x, y):
	return sum(error2(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))

def squared_error_gradient(x_i, y_i, beta):
	return [-2 * x_ij * error(x_i, y_i, beta)for x_ij in x_i]

def least_squares_fit(x, y):
	beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
	alpha = mean(y) - beta * mean(x)
	return alpha, beta

def total_sum_of_squares(y):
	return sum(v ** 2 for v in de_mean(y))

def multiple_r_squared(x, y, beta):
	sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2 for x_i, y_i in zip(x, y))
	return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)


def vector_subtract(v, w):
	return [v_i - w_i for v_i, w_i in zip(v,w)]

def scalar_multiply(c, v):
	return [c * v_i for v_i in v]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = list(zip(x, y))
    theta = theta_0                             # initial guess
    alpha = alpha_0                             # initial step size
    min_theta, min_value = None, float("inf")   # the minimum so far
    iterations_with_no_improvement = 0

    # if we ever go 100 iterations with no improvement, stop
    while iterations_with_no_improvement < 100:
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )

        if value < min_value:
            # if we've found a new minimum, remember it
            # and go back to the original step size
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # otherwise we're not improving, so try shrinking the step size
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta



def in_random_order(data):
	indexes = [i for i, _ in enumerate(data)] # create a list of indexes
	random.shuffle(indexes)
	# shuffle them
	for i in indexes:
		yield data[i]

def correlation(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(x, y) / stdev_x / stdev_y
	else:
		return 0

def standard_deviation(x):
	return math.sqrt(variance(x))
	
def variance(x):
	n = len(x)
	deviations = de_mean(x)
	return sum_of_squares(deviations) / (n - 1)

def de_mean(x):
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]

def mean(x):
	return sum(x) / len(x)

def sum_of_squares(v):
	return sum(v_i ** 2 for v_i in v)

def covariance(x, y):
	n = len(x)
	return dot(de_mean(x), de_mean(y)) / (n - 1)

def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(squared_error,
                               squared_error_gradient,
                               x, y,
                               beta_initial,
                               0.001)

random.seed(0)
beta = estimate_beta(x, y) 
print("beta", beta)
print("r-squared", multiple_r_squared(x, y, beta))
print()

