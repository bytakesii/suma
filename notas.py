def clasificar_nota(nota):
    if nota < 5:
        return "suspenso"
    elif nota < 6:          # Entre 5 y menos de 6
        return "suficiente"
    elif nota < 7:          # Entre 6 y menos de 7
        return "bien"
    elif nota < 9:          # Entre 7 y menos de 9
        return "notable"
    elif nota <= 10:        # Entre 9 y 10
        return "sobresaliente"
    else:
        return "Nota fuera de rango (debe estar entre 0 y 10)"

nota_alumno = float(input("Introduce la nota: "))

resultado = clasificar_nota(nota_alumno)
print(f"Resultado: {resultado}")