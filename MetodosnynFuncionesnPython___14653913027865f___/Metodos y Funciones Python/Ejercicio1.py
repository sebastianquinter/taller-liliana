"""Diseñar una función que calcule la media de tres números leídos del teclado y
poner un ejemplo de su aplicación."""

def calcular_media(num1, num2, num3):
    suma = num1 + num2 + num3
    media = suma / 3
    return media

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

media = calcular_media(num1, num2, num3)
print("La media de los tres números es:", media)
