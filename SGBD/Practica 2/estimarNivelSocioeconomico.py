#!/usr/bin/python

import pandas as pd
import numpy as np
import SacarOutliers as Ej2_1

#PRACTICA 5 - EJERCICIO 2.2

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#LIMITE CANTIDAD DE AMBIENTES
ambientes = np.array(range(1,9))

#FILTRO INICIAL - PRIMER CONDICION
filtro_CABA1 = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms.isin(ambientes))])

def estimarNivelSocioeconomico(df):
	df = (df.ix[(df.rooms == 3), ['place_name','price']])
	df = Ej2_1.sacarOutliers2(df)[['place_name','price']]
	mediaPorBarrio = df.groupby('place_name', as_index=False).mean().sort_values('price')
	diccionario = {}
	for x in range (0, len(mediaPorBarrio)):
		diccionario[mediaPorBarrio['place_name'].values[x]] = x+1 
	return diccionario
	
#print (estimarNivelSocioeconomico(filtro_CABA1))
	
	
