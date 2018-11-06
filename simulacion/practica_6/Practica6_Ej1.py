#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

uno = np.random.rand(100)
dos = np.random.rand(1000)
tres = np.random.rand(10000)
cuatro = np.random.rand(100000)

plt.hist(uno, bins=50)
plt.figure()
plt.hist(dos, bins=50)
plt.figure()
plt.hist(tres, bins=50)
plt.figure()
plt.hist(cuatro, bins=50)
plt.show()
