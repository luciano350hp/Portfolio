#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import re
import pymongo
from pprint import pprint

#PRACTICA 4 EJERCICIO 4-2		--	def Funcion tweetsPorPais

conn = pymongo.MongoClient()
db = conn.test
col = db.tweets

con = None
try:	
	#DICCIONARIO DE TIPO PAIS: cant. Tweets 
	def tweetsPorPais():
		result = list(col.aggregate([{"$group": { "_id": "$countryCode", "total": { "$sum": 1 }}}]) )
		diccionario1 = {}
		for row in result:
			diccionario1[str(row['_id'])] = int (row ['total'])
		print (diccionario1)
		return diccionario1

except psycopg2.DatabaseError as e:
    print(f'Error {e}')
    sys.exit(1)

finally:
    if con:
        con.close()

tweetsPorPais()
