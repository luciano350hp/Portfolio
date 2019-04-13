#!/usr/bin/python

import pandas as pd
import numpy as np

#PRACTICA 2 - EJERCICIO 3.1.1
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

promedio_depto_2amb = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms == 2), ['price']])

print(np.mean(promedio_depto_2amb))
