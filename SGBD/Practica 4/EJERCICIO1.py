#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from pprint import pprint

conn = pymongo.MongoClient()
db = conn.test
col = db.tweets

Ej1_1 = col.find({},{'_id':False, 'user.location':'1'}).limit(50)

Ej1_2 = col.distinct("lang")

Ej1_3 = col.find({'user.followers_count':{'$gt':100000}}, {'user.name':'1', 'user.description':'1', 'user.followers_count':'1', 'user.id':'1','_id':'0'})

Ej1_4 = col.find({}, {"user.id":'1', "user.name":'1', "user.followers_count":'1', '_id':'0'}).sort('user.followers_count', -1).limit(10)

ej4 = col.find({},{'user.location':'1', '_id':'1'}).limit(10)
#eja = col.aggregate([{'$group': { '_id': "$user.name", 'total': { '$sum': '1' } } }, {'$sort': {'total':'-1'} },{'$limit': '10'} ])

print("EJERCICIO 1.1", '\n')
for doc in Ej1_1:
	pprint(doc)
	print('\n')


#print("EJERCICIO 1.2", '\n')
#for doc in Ej1_2:
#	pprint(doc)

#print('\n')

#print("EJERCICIO 1.3", '\n')
#for doc in Ej1_3:
#	pprint(doc)

#print('\n')
	
#print("EJERCICIO 1.4", '\n')
#for doc in Ej1_4:
#	pprint(doc)

#print('\n')
