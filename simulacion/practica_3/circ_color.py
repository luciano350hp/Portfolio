#!/usr/bin/python

import numpy as np
import Practica3_Ej1 as Ej1
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-10, 130), ylim=(-10, 130))

patch = plt.Circle((25, -25), 2, color=(0, 0, 1))
patch2 = plt.Circle((25, -25), 2, color=(1, 0, 0))

def init():
        patch.center = (0.1, 0)
        patch2.center = (100, 0)
        ax.add_patch(patch)
        ax.add_patch(patch2)
        return patch, patch2
        
def animate(i):
    x, y = patch2.center
    a = list(range(0, 100))
    a.reverse()
    for x in a:
        try:
            patch2.center = (x/(i/10), 0)
        except ZeroDivisionError:
            print(" Division por 0")
        if patch2.center <= (0, 0):
            patch2.center = (0, 0)
        return patch, patch2

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
plt.show()  
