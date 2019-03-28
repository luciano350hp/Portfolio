#!/usr/bin/python

import re

#1er intento...
str = 'lalalal. Habia una vez. Texto:, el arbol;'
str2 = ''
match = re.search(r'(\w+\d),(\w+\d)', str)
if match:
	print (match.group(1),'',match.group(2))
print ("******")


nombres = re.findall(r'[^.,:;]+', str)
print (nombres)
for palabra in nombres:
		str2 = str2 + palabra
	
print (str2)

#print ("******")
