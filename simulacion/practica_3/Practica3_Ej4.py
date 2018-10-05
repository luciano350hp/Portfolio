#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 1
def discretizar(T, dt):
    """ La funcion devuelve el array con el dominio temporal
        , se cumple t[i] − t[i − 1] = dt. """
    t = (np.array(np.arange(0, T + dt, dt, dtype = float)))
    return(t)

def regla_tita(I, T, dt):
	""" Encuentra los valores aproximados de la funcion.
        metodo Forward Euler. """ 
	t = discretizar(T, dt)   
	valores_u = np.array([I])
	for n in range(1, len(t)):
		valores_u = np.append(valores_u, ((0.009 * t[n]) + 1) * valores_u[n-1]) #un+1
		valores_n = list(map(lambda x: (x * 40) , valores_u)) #N + 1 ( 1 pelota cada millon de personas)
		valores_n = np.around(np.array(valores_n)) #Redondeo hacia arriba
	b = discretizar(T, dt)
	print("El vector discreto es: \n ", b, "\n")
	print("Los valores de u(n+1) en los puntos t son: \n ", valores_u, "\n")
	print("Los valores de N(n+1) en los puntos t son: \n ", valores_n, "\n")
	return(valores_n)

# def grafico():
    # plt.plot((discretizar(10, 1)),(regla_tita(1, 10, 1)) , 'ro')
    # plt.axis([-0.25, 100, -0.25, 500])
    # plt.xlabel('T = 50, dt = 1')
    # plt.ylabel('θ = 0,  dt = 1')
    # plt.title('Grafico crecimiento')
    # plt.legend(('Aprox'), loc='upper left')
    # plt.show()
# grafico()

#regla_tita(1, 10, 1) 
