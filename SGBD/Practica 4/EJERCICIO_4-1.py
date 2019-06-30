#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PRACTICA 4 EJERCICIO 4.1

import re
import psycopg2
import sys
import pymongo
from pprint import pprint

conn = pymongo.MongoClient()
db = conn.test
col = db.tweets

con = None

try:
	#DICCIONARIO DE TIPO CODE2:CODE 
	con = psycopg2.connect(database='world', user='luciano')
	cur = con.cursor()
	cur2 = con.cursor()
	
	#	CONTROLO RECORRIENDO PAISES
	cur.execute('SELECT country.name, country.code FROM country;')		#TRAIGO TODOS LOS PAISES Y SUS CODIGOS DE LA BASE WORLD
	location = list(col.find({},{'user.location':'1', '_id':False}))	#TRAIGO TODAS LAS LOCATION DE LA BASE TWEETS
	paises = cur.fetchall()
	for pais in paises:				#RECORRO PAISES de tabla country	
		pais1 = pais[0]
		paisCodigo = pais[1]
		print('Pais: '+ pais1)
		print('Codigo: '+ paisCodigo)
		for loc in location:		#RECORRO LOCATION	
			user = loc['user']
			l1 = str(user['location'])			#Tomo string campo location	para poder compararlo
			l2 = re.split('; |, |- |\*|\n',l1)	#PARTICIONO location separando palabras
			for l21 in l2:						#RECORRO cada palabra de location
				if (l21==pais1):				#Si alguna de las palabras de la location es igual al pais, le asigno el pais en los nuevos campos de tweets: country y countryCode
					col.update_many({'user.location': l1, 'country': {"$exists" : False}},{'$set': {'country': pais1, 'countryCode':paisCodigo},'$currentDate': {'lastModified': True}})
		
		
	#	CONTROLO CIUDADES
	cur2.execute('SELECT city.name, country.name, country.code FROM city, country where city.countrycode=country.code;')	#TRAIGO TODAS LAS CIUDADES Y SUS PAISES DE LA BASE WORLD
	location2 = list(col.find({'country': {"$exists" : False}},{'user.location':'1', '_id':False}))							#Traigo solo las location que todavia no tienen pais
	ciudades = cur2.fetchall()
	for ciudad in ciudades:
		nombreciudad = ciudad[0]
		nombrepais = ciudad[1]
		codPais = ciudad[2]
		print('Pais: '+nombrepais)
		print('Ciudad: '+nombreciudad)
		for loc in location2:
			user = loc['user']
			l1 = str(user['location'])			#Tomo string campo location	para poder compararlo
			l2 = re.split('; |, |- |\*|\n',l1)	#PARTICIONO location separando palabras
			for l21 in l2:						#RECORRO cada palabra de location
				if (l21==nombreciudad):			#Si alguna de las palabras de la location es igual a la ciudad, le asigno el pais
					col.update_many({'user.location': l1, 'country': {"$exists" : False}},{'$set': {'country': nombrepais, 'countryCode': codPais},'$currentDate': {'lastModified': True}})
	





except psycopg2.DatabaseError as e:
    print(f'Error {e}')
    sys.exit(1)

finally:
    if con:
        con.close()
