def suma_numeros(n):
    suma = 0
    while n > 0:
        suma += n
        n -= 1
    return suma

numero = int(input("Introduce un número: "))
resultado = suma_numeros(numero)
print(resultado)
