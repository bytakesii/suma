'''
ALGORITMO: SIGNO_NUMERO
ENTRADAS: numero
SALIDA: resultado

    SI numero > 0:
        resultado = "positivo"
    SI NO SI numero < 0:
        resultado = "negativo"
    SI NO:
        resultado = "cero"
    DEVOLVER resultado
'''
def signo_numero(numero):
    """Devuelve si un número es positivo, negativo o cero."""
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"


'''
ALGORITMO: ES_BISIESTO
ENTRADAS: anio
SALIDA: resultado

    SI (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
        resultado = True
    SI NO:
        resultado = False
    DEVOLVER resultado
'''
def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
        return True
    else:
        return False


'''
ALGORITMO: MAYOR_DE_TRES
ENTRADAS: a, b, c
SALIDA: maximo

    SI a >= b and a >= c:
        maximo = a
    SI NO SI b >= a and b >= c:
        maximo = b
    SI NO:
        maximo = c
    DEVOLVER maximo
'''
def mayor_de_tres(a, b, c):
    """Devuelve el mayor de tres números sin usar max()."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


'''
ALGORITMO: CATEGORIA_ENVIO
ENTRADAS: peso_kg
SALIDA: categoria

    SI peso_kg <= 1:
        categoria = "Sobre"
    SI NO SI peso_kg <= 5:
        categoria = "Paquete pequeño"
    SI NO SI peso_kg <= 20:
        categoria = "Paquete grande"
    SI NO:
        categoria = "Voluminoso"
    DEVOLVER categoria
'''
def categoria_envio(peso_kg):
    """Clasifica un envío según su peso en kilos."""
    if peso_kg <= 1:
        return "Sobre"
    elif peso_kg <= 5:
        return "Paquete pequeño"
    elif peso_kg <= 20:
        return "Paquete grande"
    else:
        return "Voluminoso"


'''
ALGORITMO: SUMA_PARES
ENTRADAS: n
SALIDA: total

    total = 0
    PARA i EN rango(1, n + 1):
        SI i % 2 == 0:
            total = total + i
    DEVOLVER total
'''
def suma_pares(n):
    """Suma los números pares entre 1 y n."""
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total


'''
ALGORITMO: FACTORIAL_ITERATIVO
ENTRADAS: n
SALIDA: resultado

    resultado = 1
    contador = 1
    MIENTRAS contador <= n:
        resultado = resultado * contador
        contador = contador + 1
    DEVOLVER resultado
'''
def factorial_iterativo(n):
    """Calcula n! usando un bucle (versión iterativa)."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


'''
ALGORITMO: CONTAR_VOCALES
ENTRADAS: palabra
SALIDA: contador

    contador = 0
    vocales = "aeiouAEIOU"
    PARA letra EN palabra:
        SI letra in vocales:
            contador = contador + 1
    DEVOLVER contador
'''
def contar_vocales(palabra):
    """Cuenta las vocales de una palabra, sin distinguir mayúsculas."""
    contador = 0
    vocales = "aeiouAEIOU"
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador


'''
ALGORITMO: TABLA_MULTIPLICAR
ENTRADAS: numero
SALIDA: ninguna (muestra texto por pantalla)

    PARA i EN rango(1, 11):
        MOSTRAR numero + " x " + i + " = " + (numero * i)
'''
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número, del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")




'''
ALGORITMO: CALCULAR_PROMEDIO
ENTRADAS: numeros
SALIDA: promedio

    total = 0
    PARA n EN numeros:
        total = total + n
    promedio = total / longitud(numeros)
    DEVOLVER promedio
'''
def calcular_promedio(numeros):
    """Calcula la media aritmética de una lista de números."""
    total = 0
    for n in numeros:
        total += n
    return total / len(numeros)


'''
ALGORITMO: ANALIZAR_FRASE
ENTRADAS: frase
SALIDA: frase_mayus, cantidad_palabras

    frase_mayus = a_mayusculas(frase)
    palabras = separar(frase)
    cantidad_palabras = longitud(palabras)
    DEVOLVER frase_mayus, cantidad_palabras
'''
def analizar_frase(frase):
    """Devuelve la frase en mayúsculas junto con su número de palabras."""
    frase_mayus = frase.upper()
    num_palabras = len(frase.split())
    return frase_mayus, num_palabras


'''
ALGORITMO: VALIDAR_CONTRASENA
ENTRADAS: contrasena, longitud_minima
SALIDA: resultado

    SI longitud(contrasena) >= longitud_minima:
        resultado = True
    SI NO:
        resultado = False
    DEVOLVER resultado
'''
def validar_contrasena(contrasena, longitud_minima=8):
    """Comprueba si una contraseña alcanza la longitud mínima exigida."""
    if len(contrasena) >= longitud_minima:
        return True
    else:
        return False


'''
ALGORITMO: CELSIUS_A_FAHRENHEIT
ENTRADAS: celsius
SALIDA: fahrenheit

    fahrenheit = (celsius * 9 / 5) + 32
    DEVOLVER fahrenheit
'''
def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


'''
ALGORITMO: FAHRENHEIT_A_CELSIUS
ENTRADAS: fahrenheit
SALIDA: celsius

    celsius = (fahrenheit - 32) * 5 / 9
    DEVOLVER celsius
'''
def fahrenheit_a_celsius(fahrenheit):
    """Convierte una temperatura de Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9




'''
ALGORITMO: FACTORIAL_RECURSIVO
ENTRADAS: n
SALIDA: resultado

    SI n == 0 or n == 1:
        resultado = 1
    SI NO:
        resultado = n * FACTORIAL_RECURSIVO(n - 1)
    DEVOLVER resultado
'''
def factorial_recursivo(n):
    """Calcula n! llamándose a sí misma (versión recursiva)."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


'''
ALGORITMO: FIBONACCI
ENTRADAS: n
SALIDA: resultado

    SI n == 0:
        resultado = 0
    SI NO SI n == 1:
        resultado = 1
    SI NO:
        resultado = FIBONACCI(n - 1) + FIBONACCI(n - 2)
    DEVOLVER resultado
'''
def fibonacci(n):
    """Devuelve el término n de la sucesión de Fibonacci."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


'''
ALGORITMO: SUMA_LISTA
ENTRADAS: numeros
SALIDA: resultado

    SI longitud(numeros) == 0:
        resultado = 0
    SI NO:
        resultado = numeros[0] + SUMA_LISTA(numeros[1:])
    DEVOLVER resultado
'''
def suma_lista(numeros):
    """Suma los elementos de una lista de forma recursiva."""
    if len(numeros) == 0:
        return 0
    else:
        return numeros[0] + suma_lista(numeros[1:])


'''
ALGORITMO: INVERTIR_TEXTO
ENTRADAS: texto
SALIDA: resultado

    SI longitud(texto) <= 1:
        resultado = texto
    SI NO:
        resultado = texto[-1] + INVERTIR_TEXTO(texto[:-1])
    DEVOLVER resultado
'''
def invertir_texto(texto):
    """Invierte una cadena de texto de forma recursiva."""
    if len(texto) <= 1:
        return texto
    else:
        return texto[-1] + invertir_texto(texto[:-1])




'''
ALGORITMO: DIVISION_SEGURA
ENTRADAS: a, b
SALIDA: resultado

    INTENTAR:
        resultado = a / b
    CAPTURAR ZeroDivisionError:
        resultado = "Error: división entre cero"
    DEVOLVER resultado
'''
def division_segura(a, b):
    """Divide dos números controlando la división entre cero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"


'''
ALGORITMO: CONVERTIR_A_ENTERO
ENTRADAS: texto
SALIDA: resultado

    INTENTAR:
        resultado = entero(texto)
    CAPTURAR ValueError:
        resultado = "Error: no es un número"
    DEVOLVER resultado
'''
def convertir_a_entero(texto):
    """Convierte un texto a entero controlando el error de formato."""
    try:
        return int(texto)
    except ValueError:
        return "Error: no es un número"


'''
ALGORITMO: OBTENER_ELEMENTO
ENTRADAS: lista, posicion
SALIDA: resultado

    INTENTAR:
        resultado = lista[posicion]
    CAPTURAR IndexError:
        resultado = "Error: posición fuera de rango"
    DEVOLVER resultado
'''
def obtener_elemento(lista, posicion):
    """Accede a una posición de una lista controlando el error de rango."""
    try:
        return lista[posicion]
    except IndexError:
        return "Error: posición fuera de rango"


'''
ALGORITMO: CALCULADORA_SEGURA
ENTRADAS: texto_a, texto_b, operacion
SALIDA: resultado

    INTENTAR:
        a = flotante(texto_a)
        b = flotante(texto_b)
    CAPTURAR ValueError:
        DEVOLVER "Error: valor no numérico"

    SI operacion == "suma":
        resultado = a + b
    SI NO SI operacion == "division":
        INTENTAR:
            resultado = a / b
        CAPTURAR ZeroDivisionError:
            resultado = "Error: división entre cero"
    DEVOLVER resultado
'''
def calculadora_segura(texto_a, texto_b, operacion):
    """Suma o divide dos textos numéricos controlando los errores posibles."""
    try:
        a = float(texto_a)
        b = float(texto_b)
    except ValueError:
        return "Error: valor no numérico"

    if operacion == "suma":
        return a + b
    elif operacion == "division":
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: división entre cero"