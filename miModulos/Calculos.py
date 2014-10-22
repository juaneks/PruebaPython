#!/usr/bin/python
#-*- coding:UTF-8 -*-

# modulo para hacer calculos matematicos

def multiplicarTupla(mitupla,multiplicador):
	miLista = [0]
	result = 0
	for valor in mitupla:
		result = int(valor) *int(multiplicador)
		miLista.append(result)

	return miLista	
