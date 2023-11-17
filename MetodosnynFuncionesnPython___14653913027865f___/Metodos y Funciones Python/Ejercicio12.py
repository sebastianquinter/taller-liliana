"""Escribir una función que permita deducir si una fecha leída del teclado es válida."""

def es_fecha_valida(dia, mes, anio):
    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]

    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in meses_31_dias and dia > 31:
        return False
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            if dia > 29:
                return False
        elif dia > 28:
            return False
    if dia > 30:
        return False

    return True

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if es_fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")