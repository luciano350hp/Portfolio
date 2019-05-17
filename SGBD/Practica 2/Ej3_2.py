#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#PRACTICA 2 - EJERCICIO 3.2

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

print("EL CENTRO GEOGRAFICO DE CABA ES: LAT: -34.6170222, LON: -58.4451252 \n")

#FILTRO LAS PROPIEDADES DE CABA QUE ESTAN A  +/- 0.05 GRADOS DEL CENTRO GEOGRAFICO
filtro_CABA = (data.ix[(data.state_name == 'Capital Federal') & (data.lat >= -34.6670222) & 
(data.lat <= -34.5670222) & (data.lon >= -58.4951252) & (data.lon <= -58.3951252), ['lat','lon']])

print (filtro_CABA)

print("La cantidad de propiedades es:", len(filtro_CABA))

filtro_CABA.plot.scatter(x='lon', y='lat')

plt.show()
