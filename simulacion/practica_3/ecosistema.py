#!/usr/bin/python

import numpy as np
import Practica3_Ej4 as Ej4
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ParticleBox:
	def __init__(self,
				 init_state,
				 bounds = [-50, 50, -50, 50],
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
		if (not self.termino and self.time_elapsed > 3):
			#print (self.state)
			self.termino = True
			rows = self.state.shape[0]
			for i in range(0, (rows - 264)):
				#print (self.state[i,0])
				self.state[i, 1] = dt * - 100 
			for g in range(0, (rows - 264)):
				self.state[i, 1] = self.time_elapsed
				#print (self.state[i,0])

def buildBox(delta, bounds):
	#------------------------------------------------------------
	# set up initial state
	totalRows = 0
	for i in range(bounds[0]+delta, bounds[1]-delta, delta):
		for j in range(bounds[2]+delta, bounds[3]-delta, delta):
			totalRows += 1
	init_state = np.zeros((totalRows,2),dtype=float)
	row = 0
	for j in range(bounds[2]+delta, bounds[3]-delta, delta):
		for i in range(bounds[0]+delta, bounds[1]-delta, delta):
			init_state[row, 0] = i
			init_state[row, 1] = j
			row += 1
	return init_state
	
delta = 2
bounds = [0, 50, 0, 50]

box = ParticleBox(buildBox(delta, bounds), bounds, size=2.5)

bounds2 = [50, 100, 0, 50]

box2 = ParticleBox(buildBox(delta, bounds2), bounds2, size=2.5)

dt = 1. / 30 # 30fps

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 50))
particles, = ax.plot([], [], 'bo', ms=5)
particles2, = ax.plot([], [], 'ro', ms=5)

# initialization function: plot the background of each frame
def init():
	global box, box2
	particles.set_data([], [])
	particles2.set_data([], [])
	return particles,particles2,

# animation function.  This is called sequentially
def animate(i):
	global box, box2, dt, ax, fig
	box.step(dt)
	box2.step(dt)
	particles.set_data(box.state[:, 0], box.state[:, 1])
	particles.set_markersize(5)
	
	particles2.set_data(box2.state[:, 0], box2.state[:, 1])
	particles2.set_markersize(5)

	return particles,particles2,
	

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()
