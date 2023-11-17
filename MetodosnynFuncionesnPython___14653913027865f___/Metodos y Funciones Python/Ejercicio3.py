"""Diseñar el algoritmo para calcular el máximo común divisor de cuatro números
basado en una su algoritmo función mcd(el máximo común divisor de dos
números)"""

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcd_cuatro_numeros(num1, num2, num3, num4):
    mcd_1 = mcd(num1, num2)
    mcd_2 = mcd(mcd_1, num3)
    mcd_final = mcd(mcd_2, num4)
    return mcd_final

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

mcd_resultado = mcd_cuatro_numeros(num1, num2, num3, num4)
print(f"El Máximo Común Divisor de {num1}, {num2}, {num3} y {num4} es: {mcd_resultado}")

