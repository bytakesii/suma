def precio_final(a,b):
    precio= a
    impuesto= 1+b/100
    return precio * impuesto
print(precio_final(4,21))