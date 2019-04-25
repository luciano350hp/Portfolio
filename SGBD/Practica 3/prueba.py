#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from geopandas import GeoSeries, GeoDataFrame


#QUERY

world = GeoDataFrame.from_file('ne_10m_admin_0_countries.shp')
world['prueba'] = range(len(world))



# para ver los colormap, ejecutar colors.py
#world.plot(column='prueba', colormap='Greens', alpha=0.5, categorical=False, legend=False, axes=None)
#world.plot(column='prueba', colormap='binary', alpha=0.5, categorical=False, legend=False, axes=None)
# world.plot()
#world.plot(column=None, colormap='Greens', alpha=0.5, categorical=False, legend=False, axes=None)

#America del Sur

print (world['CONTINENT'].unique())

south = world[world['CONTINENT'] == 'South America']
#south.plot(column='prueba', colormap='binary', alpha=0.5, categorical=False, legend=False, axes=None)
world.plot(column='prueba', colormap='Greens', alpha=0.5, categorical=False, legend=False, axes=None)

plt.show()
