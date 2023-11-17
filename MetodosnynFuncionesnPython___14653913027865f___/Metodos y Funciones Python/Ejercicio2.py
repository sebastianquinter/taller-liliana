"""Diseñar la función FACTORIAL que calcule la factorial de un número entero
entre el rango 100 a 1.000.000."""

def FACTORIAL(n):
    if n < 0 or n > 10:
        raise ValueError("El número debe estar en el rango de 0 a 10")
    if n == 0:
        return 1
    else:
        return n * FACTORIAL(n - 1)

numero = int(input("Ingrese un número entre 0 y 10: "))
resultado = FACTORIAL(numero)
print(f"El factorial de {numero} es {resultado}")
