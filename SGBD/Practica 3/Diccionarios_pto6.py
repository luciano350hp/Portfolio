#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:
	#DICCIONARIOS DE TIPO PAIS:Población y PAIS:gnp 
	def PoblacionyGnp():
		con = psycopg2.connect(database='world', user='luciano')
		cur = con.cursor()
		cur.execute('SELECT code, population, gnp FROM country;')
		rows = cur.fetchall()
		diccionario1 = {}
		diccionario2 = {}
		for row in rows:
			diccionario1[row[0]] = row [1]
			diccionario2[row[0]] = int (row [2])
		return diccionario1, diccionario2
		
	#DICCIONARIO DE TIPO PAIS:cant. Sitios Web 
	def sitiosWeb():
		con = psycopg2.connect(database='world', user='luciano')
		cur = con.cursor()
		cur.execute('SELECT countrycode, count (id) FROM sitio GROUP BY countrycode;')
		rows = cur.fetchall()
		diccionario1 = {}
		for row in rows:
			diccionario1[row[0]] = row [1]
		return diccionario1
	
except psycopg2.DatabaseError as e:
    print(f'Error {e}')
    sys.exit(1)

finally:
    if con:
        con.close()
