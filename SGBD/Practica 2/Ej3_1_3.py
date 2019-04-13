#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#PRACTICA 2 - EJERCICIO 3.1.3

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#FILTRO LAS PROPIEDADES DE 2 AMBIENTES DE CABA POR BARRIO
filtro_CABA = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms == 2), ['place_name']])

#CALCULO LAS OCURRENCIAS POR BARRIO EN ORDEN DESCENDENTE 
ocurrenciasPorBarrio = filtro_CABA.groupby('place_name').size().sort_values(ascending=False)[0:10]

print (ocurrenciasPorBarrio)

ocurrenciasPorBarrio.plot.barh()

plt.show()


