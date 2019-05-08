#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None
try:
	con = psycopg2.connect(database='world', user='luciano')
	cur = con.cursor()
	f = open('top-1m.csv', 'r')
	csv = f.readlines()
	numeroOrden = ""
	
	for i in range (0, len(csv)):
		csv[i] = csv[i].replace('.',',')
	
	for linea in csv:
		for caracter in linea:
			if numeroOrden.isdigit():
				numeroOrden += caracter
			
		print (numeroOrden)
    #query =  "INSERT INTO items (info, city, price) VALUES (%s, %s, %s);"
    #data = (info, city, price)

    #cursor.execute(query, data)
	
	con.commit()
	

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:
	if con:
		con.close()
	if f:
		f.close()

