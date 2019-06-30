#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
from EJERCICIO_4_2_Funcion import tweetsPorPais

#PRACTICA 4 EJERCICIO 4-2		--	Usando GeoFrame de Practica 3

#LEO EL GEOFRAME
world = GeoDataFrame.from_file('ne_10m_admin_0_countries.shp')

#CREO COLUMNAS AL GEOFRAME
world['tweetsxpais'] = range (len(world))

#DICCIONARIOS (DB WORLD) DE TIPO PAIS:Tweets 
dictweets= tweetsPorPais()


#AGREGO LOS DATOS DE LA DB AL GEOFRAME
#POR CADA PAIS DEL GEOFRAME, ADJUNTO EL DATO ASOCIADO ALOJADO EN LA DB
for row in range(len(world)):
	pais = world.loc[row, ('ADM0_A3')]
	if (pais in dictweets):
		world.loc[row, ('tweetsxpais')] = dictweets[pais]


#GRAFICOS		
world.plot(column = 'tweetsxpais', cmap='seismic', alpha=0.5, categorical=False, legend=True, ax=None)
plt.title('Choropleth Tweets Mundial')

plt.show()
