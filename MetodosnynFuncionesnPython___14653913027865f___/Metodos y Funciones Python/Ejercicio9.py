"""Escribir una función booleana Digito que determine si un carácter es uno de los dígitos 0 al 9."""

def es_digito(caracter):
    if caracter >= '0' and caracter <= '9':
        return True
    else:
        return False

caracter = input("Ingrese un carácter: ")

if es_digito(caracter):
    print(f"{caracter} es un dígito")
else:
    print(f"{caracter} no es un dígito")