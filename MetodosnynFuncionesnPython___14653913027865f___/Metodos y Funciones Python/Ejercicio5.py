"""Diseñar una función que calcule X ́n para X, variable real y n variable entera."""

def calcular_potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

base = float(input("Ingrese el valor de X (base real): "))
exponente = int(input("Ingrese el valor de n (exponente entero): "))

resultado_potencia = calcular_potencia(base, exponente)
print(f"{base}^{exponente} es igual a {resultado_potencia}")
