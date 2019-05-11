#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import Ej4_1

con = None
try:
	con = psycopg2.connect(database='world', user='luciano')
	cur = con.cursor()
	f = open('top-1m.csv', 'r')
	csv = f.readlines()
	
	#SE AGREGAN CLAVES AL DICCINARIO 
	Ej4_1.diccionario['UK'] = 'GBR'
	Ej4_1.diccionario['GG'] = 'GBR'
	Ej4_1.diccionario['IM'] = 'GBR'
	
	for i in range (0, len(csv)):
		csv[i] = csv[i].replace('.',',')
		csv[i] = csv[i].strip()
	
	for linea in csv:
		linea = linea.split(',')
		id = linea[0]
		entidad = linea[1]
		tipo_entidad = linea[2]
		if len(linea) == 4:
			pais = linea [3]
			if (pais.upper() in Ej4_1.diccionario):
				countrycode = Ej4_1.diccionario[pais.upper()]
				query =  "INSERT INTO sitio (id, entidad, tipo_entidad, pais, countrycode)  VALUES (%s, %s, %s, %s, %s);"
				data = (id, entidad, tipo_entidad,pais,countrycode)
				cur.execute(query, data)
		else:
			if (tipo_entidad.upper() in Ej4_1.diccionario):
				countrycode = Ej4_1.diccionario[tipo_entidad.upper()]
				query =  "INSERT INTO sitio (id, entidad, tipo_entidad,countrycode) VALUES (%s, %s, %s, %s);"
				data = (id, entidad, tipo_entidad,countrycode)
				cur.execute(query, data)
			else:
				query =  "INSERT INTO sitio (id, entidad, tipo_entidad) VALUES (%s, %s, %s);"
				data = (id, entidad, tipo_entidad)
				cur.execute(query, data)
	con.commit()
	

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:
	if con:
		con.close()
	if f:
		f.close()

