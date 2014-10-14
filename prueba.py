#usando ninja IDE

def sacaIVA (valor,iva):
    total =0
    if valor > 100:
        total = valor * iva
    else:
        total = "solo a valores mayor a 100 se saca IVA"
    return total

valor = input("ingrese el valor :")
total = sacaIVA(valor,1.12)

print "el total es :",total




