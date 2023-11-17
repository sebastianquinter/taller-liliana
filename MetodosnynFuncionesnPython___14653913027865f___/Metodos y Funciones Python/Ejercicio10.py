"""Diseñar una función que permita devolver el valor absoluto de un numero."""

def valor(numero):
    valor_absoluto = abs(numero)
    return valor_absoluto

numero = int(input('Ingresa un número: '))
total = valor(numero)

print(f"El valor absoluto de {numero} es: {total}")