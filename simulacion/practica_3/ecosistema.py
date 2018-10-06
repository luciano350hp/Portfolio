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
		self.pelotas = Ej4.regla_tita(1, 30, 1)
		self.totalp = self.state.shape[0]
		for i in range(0, self.totalp):
			self.state[i, 1] = -1 #Borro el tablero inicial
		
	def step(self, dt):
		"""step once by dt seconds"""
		self.time_elapsed += dt
		for a in self.pelotas:
			a= int(a)
			for j in range (0, a):
				self.state[j, 0] = self.init_state[j, 0]
				self.state[j, 1] = self.init_state[j, 1]
				
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
bounds = [0, 100, 0, 100]
box = ParticleBox(buildBox(delta, bounds), bounds, size=2.5)
dt = 1. /30 # 30fps

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 110), ylim=(0, 110))
particles, = ax.plot([], [], 'bo', ms=5)
particles2, = ax.plot([], [], 'ro', ms=5)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
time_text2 = ax.text(0.02, 0.90, '', transform=ax.transAxes)
time_text3 = ax.text(0.02, 0.85, '', transform=ax.transAxes)

# initialization function: plot the background of each frame
def init():
	global box
	particles.set_data([], [])
	time_text.set_text('')
	time_text2.set_text('')
	time_text3.set_text('')
	return particles,

pelotas = Ej4.regla_tita(1, 30, 1)
# animation function.  This is called sequentially
def animate(i):
	global box,  dt, ax, fig
	box.step(dt)
	plt.scatter(box.state[i, 0], box.state[i, 1], c = 'b')
	time_text.set_text('Población Actual = %.1f millones' % i)
	año = 0
	for x in pelotas:
		if (i == x):
			time_text3.set_text('Año = %.1f' % año)
			time_text2.set_text('Poblacion por año = %.1f millones' % x)
		año += 1
	particles.set_markersize(5)
	return particles,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames= int(pelotas[30]), interval=100, repeat=True)

plt.show()
