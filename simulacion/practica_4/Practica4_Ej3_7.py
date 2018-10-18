#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#PASO 1 
def discretizar(L1, T1, deltax, deltat):
    """ La funcion devuelve los array con el dominio
        de x y t discretizados. """
    t = (np.array(np.arange(0, T + deltat, deltat, dtype = float)))
    x = (np.array(np.arange(0, L + deltax, deltax, dtype = float)))
    return(t, x)

#FIJO VARIABLES GLOBALES
L = 10
T = 500
deltax = 1
deltat = 1
c = 1
C = c * (deltat/deltax)
vec = discretizar(L, T, deltax, deltat)

print("El vector discreto es: \n ", vec, "\n")

I = [1,1,0,0,0,0,0,0,0,0,0]
u = np.zeros((T//deltat+1,L//deltax+1),dtype=float)

print("cantidad de filas: ", len(u)) 
print("cantidad de columnas: ", len(u[1]))


#PASO 2
def tiempo0():
	""" Calcula u(x,t) en t = 0.
		u(x, 0) = I(x). """
	global u, vec
	u[0] = I
	u[0][0] = 0 #Por condicion inicial de borde
	u[0][-1] = 0 #Por condicion inicial de borde

tiempo0()

#PASO 3
def tiempo1():
	""" Calcula u(x,t) en t = 1. """
	for i in range (1, len(vec[1])-1):
		u[1][i] = u[0][i] + ((C**2/2) * (u[0][i+1]- 2*u[0][i] + u[0][i-1]))

tiempo1() 

#PASO 4
def recurrencia():
	""" Calcula u(x,t) desde t = 2 hasta el final. """
	for j in range (2, len(vec[0])):
		for g in range (1, len(vec[1])-1):
			u[j][g] = -u[j-2][g] + 2 * u[j-1][g] +((C**2) * (u[j-1][g+1] - 2 * u[j-1][g] + u[j-1][g-1]))
			
recurrencia()

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-2, 20), ylim=(-10, 10))

ploteo, = ax.plot(vec[1], u[0], 'b-', ms=5)

def init():
    global ploteo
    ploteo.set_data(vec[1], u[0])
    return ploteo,
	
# animation function.  This is called sequentially
def animate(n):
	global ax, fig, ploteo
	ploteo.set_data(vec[1], u[n])
	return ploteo,
	
anim = animation.FuncAnimation(fig, animate, frames= len(vec[0]), interval=100, repeat=True)

plt.show()
