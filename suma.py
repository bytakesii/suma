"""
ALGORITMO: SUMA_NUMEROS
ENTRADAS: n
SALIDA: suma

suma = 0
MIENTRAS n > 0:
    suma = suma + n
    n = n - 1
DEVOLVER suma

LLAMADAS:
SUMA_NUMEROS(5) -> 15
"""

def suma_numeros(n):
    suma = 0
    while n > 0:
        suma += n
        n -= 1
    return suma

numero = int(input("Introduce un número: "))
resultado = suma_numeros(numero)
print(resultado)
