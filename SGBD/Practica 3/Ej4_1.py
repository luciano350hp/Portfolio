#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PRACTICA 3 EJERCICIO 4.1

import psycopg2
import sys

con = None

try:

	con = psycopg2.connect(database='world', user='luciano')
	cur = con.cursor()
	cur.execute('SELECT code2, code FROM country;')
	rows = cur.fetchall()
	diccionario = {}
	for row in rows:
		diccionario[row[0]] = row [1] 
	#print(diccionario)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()
