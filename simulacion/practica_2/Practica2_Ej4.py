#!/usr/bin/python

import numpy as np
from random import randint, uniform,random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ParticleBox:
        def __init__(self,
                                init_state = [[0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0]],
                                bounds = [0, 50, 0, 50],
                                size = 0.04):
                self.init_state = np.asarray(init_state, dtype=float)
                self.size = size
                self.state = self.init_state.copy()
                self.time_elapsed = 0
                self.bounds = bounds
                self.chocaron = False
        def step(self, dt):
                """step once by dt seconds"""
                self.time_elapsed += dt
                tiempo = self.time_elapsed
                # update positions
                self.state[:, 0] += dt * self.state[:, 2]
                self.state[:, 1] += dt * self.state[:, 3]
                
                #Aca vienen los dos for anidados.
                for particula in range(0, len(self.state)):
                    for particula1 in range(particula+1, len(self.state)):
                        posx1 = self.state[particula, 0] 
                        posx2 = self.state[particula1, 0]
                        posy1 = self.state[particula, 1]
                        posy2 = self.state[particula1, 1]

                        #-1- Vector normal de dos particulas
                        normal = [(posx2 - posx1), (posy2 - posy1)]

                        #-2- Vector unitario normal
                        modulo_normal = np.linalg.norm(normal)

                        condicion = modulo_normal <= (2 * self.size)
                        #if (not self.chocaron and condicion):
                        if (condicion):
                    
                            vector_unitario = normal/modulo_normal
                            #-3- Vector tangente unitario
                            vector_tang = [-vector_unitario[1], vector_unitario[0]]

                            #-4- Vector velocidad (particula 1 y 2)
                            vector_vel1 = [(self.state[particula, 2]), (self.state[particula, 3])]
                            vector_vel2 = [(self.state[particula1, 2]), (self.state[particula1, 3])]

                            #-5- Velocidades normales y tangenciales
                            veloc_1_normal = np.dot(vector_unitario, vector_vel1)
                            veloc_2_normal = np.dot(vector_unitario, vector_vel2)

                            v1n = veloc_1_normal
                            v2n = veloc_2_normal

                            veloc_1_tang = np.dot(vector_tang, vector_vel1)
                            veloc_2_tang = np.dot(vector_tang, vector_vel2)

                            print("Colisionaron a los: ",tiempo,"Segundos")
                            veloc_1_normal = v2n
                            veloc_2_normal = v1n
                    
                            veloc_1_normalv = np.dot(veloc_1_normal, vector_unitario)
                            veloc_2_normalv = np.dot(veloc_2_normal, vector_unitario)

                            veloc_1_tangv = np.dot(veloc_1_tang, vector_tang)
                            veloc_2_tangv = np.dot(veloc_2_tang, vector_tang)

                            vector_vel1 = veloc_1_normalv + veloc_1_tangv
                            vector_vel2 = veloc_2_normalv + veloc_2_tangv

                            [(self.state[particula, 2]), (self.state[particula, 3])] = vector_vel1
                            [(self.state[particula1, 2]), (self.state[particula1, 3])] = vector_vel2

                            print("Veloc1", vector_vel1, "Veloc2", vector_vel2)
                            #self.chocaron = False

                # check for crossing boundary                
                crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size)
                crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size)
                crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size)
                crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size)               
                self.state[crossed_x1 | crossed_x2, 2] *= -1
                self.state[crossed_y1 | crossed_y2, 3] *= -1
 
#---------------------------------------------------------------------------
# set up initial state
dt = 1. /30

#init_state = init_state = np.zeros((2,4), dtype=float)
init_state = np.random.randint(50, size=(50, 4), dtype=int)

box = ParticleBox(init_state, size=1)
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0, 50))
particles, = ax.plot([], [], 'bo', ms=5)
# initialization function: plot the background of each frame
def init():
	global box
	particles.set_data([], [])
	return particles,
# animation function.  This is called sequentially
def animate(i):
        global box, dt, ax, fig                                                         
        box.step(dt)
        particles.set_data(box.state[:, 0], box.state[:, 1])
        particles.set_markersize(5)
        return particles,
	

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
plt.show()
