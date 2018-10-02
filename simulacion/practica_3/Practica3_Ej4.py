#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 1
def discretizar(T, dt):
    """ La funcion devuelve el array con el dominio temporal
        , se cumple t[i] − t[i − 1] = dt. """
    t = (np.array(np.arange(0, T + dt, dt, dtype = float)))
    return(t)

def regla_tita(I, a, T, dt):
    """ Encuentra los valores aproximados de la funcion.
        metodo Forward Euler. """ 
    t = discretizar(T, dt)   
    valores_u = np.array([I])
    for n in range(1, len(t)):
        valores_u = np.append(valores_u, ((0.009 * t[n])  + 1) * valores_u[n-1]) 
    b = discretizar(T, dt)
    print("El vector discreto es: \n ", b, "\n")
    print("Los valores de la funcion en los puntos t son: \n ", valores_u, "\n")
    return(valores_u)

def grafico():
    plt.plot((discretizar(50, 1/30)),(regla_tita(5, 2, 50, 1/30)) , 'r')
    plt.axis([-0.25, 15, -0.25, 3000])
    plt.xlabel('T = 50, dt = 1/30')
    plt.ylabel('θ = 0,  dt = 1/30')
    plt.title('Grafico crecimiento')
    plt.legend(('Aprox'), loc='upper left')
    plt.show()
#grafico()

