"""Realizar un procedimiento que obtenga la división entera y el 
resto de la misma utilizando la únicamente los operadores suma y resta:"""

def division_y_resto(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    resto = dividendo
    return cociente, resto

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

cociente, resto = division_y_resto(dividendo, divisor)

print(f"Cociente: {cociente}")
print(f"Resto: {resto}")