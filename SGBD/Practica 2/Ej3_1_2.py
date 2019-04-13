#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#PRACTICA 2 - EJERCICIO 3.1.2

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#FILTRO LAS PROPIEDADES DE CABA POR AMBIENTES
filtro_CABA = (data.ix[(data.state_name == 'Capital Federal'), ['rooms']])

#CALCULO LAS OCURRENCIAS POR AMBIENTE QUITANDO OUTLIERS
ocurrenciasPorAmbiente = filtro_CABA.groupby('rooms').size()[0:8]

print (ocurrenciasPorAmbiente)

ocurrenciasPorAmbiente.plot.bar()

plt.show()


