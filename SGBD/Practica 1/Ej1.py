#!/usr/bin/python3

import re

#str = 'PXXII'


def esNumeroRomano():
	c = input('ingrese cadena: ')
	match = re.search(r'[XIVDMLC]+', c)
	try:
		if match.group() == c:
			print ('TRUE')
		else:
			print ('FALSE')
	except:
		print ('FALSE')

esNumeroRomano()



