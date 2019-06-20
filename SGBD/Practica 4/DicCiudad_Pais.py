#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PRACTICA 3 EJERCICIO 4.1

import psycopg2
import sys
import pymongo
from pprint import pprint

conn = pymongo.MongoClient()
db = conn.test
col = db.tweets

con = None
#db.tweets.update({user.location: /+ +/},{user.location: /+ +/},{user.location: /+ +/},{user.location: /+ +/},{$set: {country: + +}}, {multi: true})

try:
	#DICCIONARIO DE TIPO CODE2:CODE 
	con = psycopg2.connect(database='world', user='luciano')
	cur = con.cursor()
	cur2 = con.cursor()
	location = col.find({},{'user.location':'1', '_id':False})
	#cur.execute('SELECT city.name, city.district, city.countrycode, country.name FROM country,city where city.countrycode = country.code;')
	cur.execute('SELECT country.name FROM country;')
	rows = cur.fetchall()
	for row in rows:
		for loc in location:
			l2 = loc.split(/\s+/)
			for l21 in l2:
				

			#col.update({'user.location': /row[0]/},{'user.location': /row[1]/},{'user.location': /row[2]/},{'user.location': /row[3]/},{'$set': {'country': row[3]},'$currentDate': {'lastModified': True}})
		#print (row[0])



except psycopg2.DatabaseError as e:
    print(f'Error {e}')
    sys.exit(1)

finally:
    if con:
        con.close()
