#!/usr/bin/env python
import numpy as np

#Ejercicio 1
def discretizar(T, dt):
    """ La funcion devuelve el array con el dominio temporal
        , se cumple t[i] − t[i − 1] = dt. """
    t = (np.array(np.arange(0, T + dt, dt, dtype = float)))
    return(t)

def regla_tita(I, a, T, dt, θ):
    """ Encuentra los valores aproximados de la funcion y la derivada. """ 
    t = discretizar(T, dt)   
    valores_u = np.array([I])
    for n in range(1, len(t)):
        numerador = (1 - ((1 - θ) * a * (t[n] - t[n-1])))
        denominador = (1 + (θ * a * (t[n] - t[n-1]))) 
        valores_u = np.append(valores_u, ((numerador / denominador) * valores_u[n-1])) 
    derivada_u = list(map(lambda x: (x * -a) , valores_u)) # u'(t) = -au(t) 
    derivada_u = np.array(derivada_u)
    b = discretizar(T, dt)
    print("El vector discreto es: \n ", b, "\n")
    print("Los valores aprox de la funcion en los puntos t son: \n ", valores_u, "\n")
    print("Los valores aprox de la derivada en los puntos t son: \n ", derivada_u, "\n")
    return(valores_u)
