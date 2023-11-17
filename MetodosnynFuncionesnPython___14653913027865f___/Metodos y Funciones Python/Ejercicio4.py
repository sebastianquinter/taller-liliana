"""Diseñar una función que encuentro el mayor de dos números enteros."""

def numero_mayor(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

resultado = numero_mayor(num1, num2)

print(f"El mayor entre {num1} y {num2} es: {resultado}")
