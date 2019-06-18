#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PRACTICA 3 EJERCICIO 4.1

import psycopg2
import sys

con = None

try:
	#DICCIONARIO DE TIPO CODE2:CODE 
	con = psycopg2.connect(database='world', user='luciano')
	cur = con.cursor()
	cur2 = con.cursor()
	cur.execute('SELECT district, countrycode FROM city;')
	cur2.execute('SELECT name, countrycode FROM city;')
	rows = cur.fetchall()
	rows2 = cur2.fetchall()
	diccionario = {}
	for row in rows:
		diccionario[row[0]] = row [1] 
	for row in rows2:
		diccionario[row[0]] = row [1]
	print(diccionario['Florida'])
	print(diccionario['Miami'])
	print(diccionario['Buenos Aires'])
	print(diccionario['Mar del Plata'])
	print(diccionario['Córdoba'])
	print(diccionario['Río Cuarto'])
	print(diccionario['Houston'])




except psycopg2.DatabaseError as e:
    print(f'Error {e}')
    sys.exit(1)

finally:
    if con:
        con.close()
