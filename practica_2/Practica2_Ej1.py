#!/usr/bin/python

import numpy as np
from time import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ParticleBox:
        def __init__(self,
                                init_state = [[0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0]],
                                bounds = [-100, 100, -100, 150],
                                size = 0.04):
                self.init_state = np.asarray(init_state, dtype=float)
                self.size = size
                self.state = self.init_state.copy()
                self.time_elapsed = 0
                self.bounds = bounds
                self.termino = False
        def step(self, dt):
                """step once by dt seconds"""
                self.time_elapsed += dt

		# update positions
                if (not self.termino):
                    self.state[:, 3] += ((dt) * -9.81)
                    self.state[:, 1] += dt * self.state[:, 3]
                if  (not self.termino and self.state[:, 1] <= 0):
                    self.state[:, 3] = 0
                    self.termino = True
                    print(self.time_elapsed)


                #self.state[:, 1] += ((dt**2) * -4.905) 
		# check for crossing boundary
                crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size)
                crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size)
                crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size)
                crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size)

                self.state[crossed_x1 | crossed_x2, 2] *= 0
                self.state[crossed_y1 | crossed_y2, 3] *= 0
#---------------------------------------------------------------------------
# set up initial state
dt = 1. /30
init_state = np.zeros((1,4),dtype=float)
init_state[0, 0] = 0
init_state[0, 1] = 100
init_state[0, 2] = 0
init_state[0, 3] = 0

box = ParticleBox(init_state, size=2.5)
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 150))
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
