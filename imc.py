def calcular_imc(peso, altura):
    imc = peso / (altura**2)

    if imc <= 18.5:
        categoria = "bajo peso"
    elif imc <= 25:
        categoria = "normal"
    else:
        categoria = "obeso"

    return imc, categoria

peso = float(input("Introduce tu peso (kg): "))
altura = float(input("Introduce tu altura (m): "))

imc_resultado, cat_resultado = calcular_imc(peso, altura)
print(f"Tu IMC es {imc_resultado:.2f} y tu categoría es: {cat_resultado}")