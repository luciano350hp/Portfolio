#!/usr/bin/python

import pandas as pd
import numpy as np

#PRACTICA 5 - EJERCICIO 2.1

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#LIMITE CANTIDAD DE AMBIENTES
ambientes = np.array(range(1,9))

#FILTRO INICIAL - PRIMER CONDICION
filtro_CABA1 = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms.isin(ambientes))])

def sacarOutliers(df, barrio, ambientes):
	df = (df.ix[(df.place_name == barrio) & (df.rooms == ambientes)])
	media = df['price'].mean()
	desvio =   df['price'].std()
	condicion1 = media + (3 * desvio)
	condicion2 = media - (3 * desvio)
	filtro_Outliers = (df.ix[(df.price < condicion1) & (df.price > condicion2)])
	return filtro_Outliers

def sacarOutliers2(df):
	media = df['price'].mean()
	desvio =   df['price'].std()
	condicion1 = media + (3 * desvio)
	condicion2 = media - (3 * desvio)
	filtro_Outliers = (df.ix[(df.price < condicion1) & (df.price > condicion2)])
	return filtro_Outliers

#print (sacarOutliers(filtro_CABA1, 'Belgrano', 7))
#print (sacarOutliers2 (filtro_CABA1))
