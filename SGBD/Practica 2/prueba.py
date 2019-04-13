#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

print (obj2)

obj2 [0] = 1

print (obj2) 

obj2 [['c','d']] *= 2

print (obj2)
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b');
ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1');
df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax);

plt.show()
