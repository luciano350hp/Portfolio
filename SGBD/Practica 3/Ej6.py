#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
from Diccionarios_pto6 import PoblacionyGnp, sitiosWeb

#PRACTICA 3 EJERCICIO 6

#LEO EL GEOFRAME
world = GeoDataFrame.from_file('ne_10m_admin_0_countries.shp')

#CREO 3 COLUMNAS AL GEOFRAME
world['population'] = range(len(world))
world['gnp'] = range(len(world))
world['sitios'] = range(len(world))

#DICCIONARIOS (DB WORLD) DE TIPO PAIS:Población, PAIS:gnp Y PAIS:cant. Sitios Web 
dicPopulation, dicGnp = PoblacionyGnp()
dicSitios = sitiosWeb()

#AGREGO LOS DATOS DE LA DB AL GEOFRAME
#POR CADA PAIS DEL GEOFRAME, ADJUNTO EL DATO ASOCIADO ALOJADO EN LA DB
for row in range(len(world)):
	pais = world.loc[row, ('ADM0_A3')]
	if (pais in dicPopulation):
		world.loc[row, ('population')] = dicPopulation[pais]
		world.loc[row, ('gnp')] = dicGnp[pais]
	if (pais in dicSitios):
		world.loc[row, ('sitios')] = dicSitios[pais]

#GRAFICOS		
world.plot(column = 'population', cmap='seismic', alpha=0.5, categorical=False, legend=True, ax=None)
plt.title('Choropleth Población Mundial')
world.plot(column = 'gnp', cmap='brg', alpha=0.5, categorical=False, legend=True, ax=None)
plt.title('Choropleth Producto Bruto Mundial')
world.plot(column = 'sitios', cmap='jet', alpha=0.5, categorical=False, legend=True, ax=None)
plt.title('Choropleth Cantidad Sitios Web Mundial')
plt.show()
