#!/usr/bin/python

import pandas as pd
import numpy as np
import SacarOutliers as Ej2_1
import estimarNivelSocioeconomico as Ej2_2

#PRACTICA 5 - EJERCICIO 2.3

#LEO EL CSV
data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#LIMITE CANTIDAD DE AMBIENTES
ambientes = np.array(range(1,9))

#FILTRO INICIAL - PRIMER CONDICION
filtro_CABA1 = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms.isin(ambientes))])

#FILTRO VALORES NAN (NULL)
filtro_CABA1 = (filtro_CABA1.ix[(filtro_CABA1.rooms.notnull()) & (filtro_CABA1.price.notnull()) & (filtro_CABA1.surface_total_in_m2.notnull())])

#SACO OUTLIERS
filtro_CABA1 = Ej2_1.sacarOutliers2(filtro_CABA1)

#AGREGO LA COLUMNA AL DATA FRAME
filtro_CABA1['NS'] = range(len(filtro_CABA1))

#DICCIONARIO NIVEL SOCIOECONOMICO
dicNS = Ej2_2.estimarNivelSocioeconomico(filtro_CABA1)

#print(dicNS)

#AGREGO LOS DATOS DEL DICCIONARIO A DB DATAFRAME
#POR CADA PROPIEDAD, ADJUNTO EL DATO  NS DEL DICCIONARIO

for row in range(len(filtro_CABA1)):
	barrio = filtro_CABA1['place_name'].values[row]                                                                    
	if (barrio in dicNS):
		filtro_CABA1['NS'].values[row]  = dicNS[barrio]
	
#ELIMINO LAS PROP QUE NO POSEEN BARRIO EN estimarNivelSocioeconomico()
filtro_CABA1 = (filtro_CABA1.ix[(filtro_CABA1.NS <= 60)])
		
df = filtro_CABA1[['NS','surface_total_in_m2', 'rooms', 'price']]
df.to_csv('dataset.csv', index = False) 
