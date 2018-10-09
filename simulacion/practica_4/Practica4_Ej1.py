#!/usr/bin/python

import numpy as np 

#Ejercicio 1
def discretizar(L, T, delta):
    """ La funcion devuelve los array con el dominio
        de x y t discretizados. """
    t = (np.array(np.arange(0, T + delta, delta, dtype = float)))
    x = (np.array(np.arange(0, L + delta, delta, dtype = float)))
    return(t, x)
    
b = discretizar(20, 5, 0.5)
print("El vector discreto es: \n ", b, "\n")
