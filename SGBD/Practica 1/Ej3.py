#!/usr/bin/python

import re

str = 'lalalal. Habia una vez. Texto:, el arbol;'
str2 = ''

nombres = re.findall(r'[^.,:;]+', str)
for palabra in nombres:
		str2 = str2 + palabra
print (str2)
print ("******")
