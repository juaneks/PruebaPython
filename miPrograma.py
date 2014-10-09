#!/usr/bin/python
# programa de ejemplo en python

iva = 12/100
print("programa que suma 2 numeros")

a= input("ingrese el numero 1 :")
b = input("ingrese el numero 2:")
suma = a+b
print "el resultado de la suma es :",suma
if suma > 100:
	print("la suma es mayor a 100, se cobrara IVA")
	
arreglo = [3,4,6,78,10]
print "este es un arreglo :",arreglo
print "arreglo rebanado :",arreglo[:2]	