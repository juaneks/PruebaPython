#!/usr/bin/python
#-*- coding: utf8 -*-
# usando ninja IDE

def sacaIVA(valor,iva):
    total =0.0
    if valor > 100:
        total = valor * iva
    else:
        total = "solo a valores mayor a 100 se saca IVA"
    return total

# valor = raw_input("ingrese el valor :")
# total2 = sacaIVA(valor,1.12)

# print "el total es :",total2

 #  otro ejercicio

mitupla = ("juan avelino",22)
nom,edad = mitupla

print mitupla

miList = [01,"leche",23.45]

a =raw_input("ingrese codigo :")
b = raw_input("ingrese nombre :")
c = raw_input("ingrese el precio :")
diccionario = {'codigo ':a, 'descripcion':b, 'precio':c}
print "el precio que ingreso es : ",diccionario['precio']
print "modificando..."
diccionario['precio'] = miList[-1]

print "el precio ya modificado es :", diccionario['precio']-1






