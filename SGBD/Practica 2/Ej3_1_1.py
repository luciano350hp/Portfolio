#!/usr/bin/python

import pandas as pd
import numpy as np

#PRACTICA 2 - EJERCICIO 3.1.1

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#FILTRO LAS PROPIEDADES DE 2 AMBIENTES DE CABA POR PRECIO
precio_deptos_2amb = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms == 2), ['price']])

print(precio_deptos_2amb)

#CALCULO EL VALOR MEDIO DEL PRECIO DE LAS PROPIEDADES DE 2 AMBIENTES DE CABA
print("El valor medio de las propiedades de CABA de 2 ambientes es:\n", np.mean(precio_deptos_2amb))
