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
L = 20
T = 10
deltax = 1
deltat = 1
c = 1
C = c * (deltat/deltax)
vec = discretizar(L, T, deltax, deltat)
print("El vector discreto es: \n ", vec, "\n")
#I = np.sin(vec[1])
u = np.zeros((T//deltat+1,L//deltax+1),dtype=float)
print ("u es", u )
print("cantidad de filas: ", len(u))
print("cantidad de columnas: ", len(u[1]))


#PASO 2
def tiempo0():
	""" Calcula u(x,t) en t = 0.
		u(x, 0) = I(x). """
	global u, vec
	u[0] = np.sin(vec[1]) #Producto Vectorial
	u[0][0] = 0 #Por condicion inicial de borde
	u[0][-1] = 0 #Por condicion inicial de borde
	print ("u0 es", u )

g = tiempo0()

#PASO 3
def tiempo1(u):
	u1 = np.copy(u)
	for i in range (1, len(u)-2):
		u1[i] = u[i] + ((C**2/2) * (u[i+1]- 2*u[i] + u[i-1]))
	print("La funcion u1 vale: \n ", u1, "\n")
	return u1
	
b = tiempo1(u) 

#PASO 4

# def recurrencia():
	# vector = [u, b]
	# for g in range (1, len(vec[1])-2):
		# u2 = []
		# for j in range (2, len(vec[0])-1):
			# u2.append(-vector[j-2][g])
	# vector = np.asarray(vector)
	# print("El vector es", vector)

# rec = recurrencia()

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, 40), ylim=(-1.20, 1.20))

# initialization function: plot the background of each frame

# animation function.  This is called sequentially
def animate(i):
	""" Genera una pelota por intervalo.
		Se muestra en pantalla la poblacion y los años
		correspondientes al crecimiento exponencial. """
	global ax, fig
	if (i <= 0):
		plt.clf()
		plt.plot(u, c = 'b')
	elif (i == 1):
		plt.clf()
		plt.plot(b, c = 'r')
	else:
		plt.clf()
		# u0 = np.copy(u)
		# u1 = np.copy(b)
		# vector = [u0, u1]
		# print("El vector vale: \n ", vector, "\n")
		#for i in range (2, len(vec[0])):
		#	for g in range (1, len(vec[1])-2):
		#		for j in range (2, len(vec[1])-2):
		#			vector.append(-vector[j-2][g] + 2 * vector[j-1][g] +((C**2) * (vector[j-1][g+1]- 2*vector[j-1][g] + vector[j-1][g-1])))
		#vector = np.asarray(vector)
		# print("El vector vale: \n ", vector, "\n")
			
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames= len(vec[0]), interval=500, repeat=True)

plt.show()
