#!/usr/bin/env python
import numpy as np
import Practica3_Ej1 as Ej1
import matplotlib.pyplot as plt

def main():
    """ Calcula aproximacion Crank-Nicholson con I = 100, Ts = 0, dt = 0.1, T = 100. """
    print("La solucion aproximada a = 0.5 es: \n ")
    Ej1.regla_tita(100, 0.5, 100, 0.1, 0.5)
    print("La solucion aproximada a = 1 es: \n ")
    Ej1.regla_tita(100, 1, 100, 0.1, 0.5)
    print("La solucion aproximada a = 2 es: \n ")
    Ej1.regla_tita(100, 2, 100, 0.1, 0.5)
main()
