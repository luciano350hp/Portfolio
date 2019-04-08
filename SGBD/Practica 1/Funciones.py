#!/usr/bin/python

import re
import collections

def textoSinPuntuacion(textoV1):
	texto = ""
	listaPalabras = re.findall(r'[^.,:;<>_()¿?!\'\[\]\-]+', textoV1)
	for palabra in listaPalabras:
		texto = texto + palabra
	return texto

def quitarBarraN(lista):
	listaSinN = list(map(lambda x: x.strip() , lista))
	return listaSinN

def listaOcurrencias(listaPalabras):
	listaOcurrenciasPalabras = collections.Counter(listaPalabras)
	return listaOcurrenciasPalabras

def textoSinPalabrasProhibidas(textoV2, listaProhibidas2):
	
	#	PASAR PALABRAS A MINUSCULAS
	textoV1 = textoV2.lower()
	#	DESCARTAR SIGNOS DE PUNTUACION
	texto = textoSinPuntuacion(textoV1)
	texto = texto.replace('\n',"")

	#	LISTA DE PALABRAS PROHIBIDAS
	listaProhibidas = quitarBarraN(listaProhibidas2)
	
	#	ELIMINO DEL TEXTO LAS PALABRAS PROHIBIDAS 
	for palabra in listaProhibidas:
		texto = texto.replace(palabra,"")
	return texto, listaProhibidas
	
	
	

		
