#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#PRACTICA 2 - EJERCICIO 3.3.1

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#FILTRO LAS PROPIEDADES DE 3 AMBIENTES DE LAS 5 CIUDADES
filtro_5_Ciudades = (data.ix[(data.rooms == 3) & ((data.state_name == 'Capital Federal')| (data.place_name == 'Rosario')
| (data.place_name == 'Córdoba') | (data.place_name == 'La Plata') |(data.place_name == 'Mar del Plata'))
,['state_name','price']])

print(filtro_5_Ciudades)

#GENERO BOXPLOT DE LOS PRECIOS DE LOS DEPTOS 3 AMB DE LAS 5 CIUDADES
grafico = filtro_5_Ciudades.boxplot(column=['price'], by=['state_name'])
labels = ['La Plata','Mar del Plata','Capital Federal','Córdoba','Rosario']
grafico.set_xticklabels(labels)

plt.show()
