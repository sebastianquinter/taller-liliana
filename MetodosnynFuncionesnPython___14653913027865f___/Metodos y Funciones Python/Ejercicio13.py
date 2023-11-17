"""Escribir el algoritmo que permita obtener el número de elementos positivos de una tabla"""

def numeros_positivos(tabla):
  contador = 0
  for elemento in tabla:
    if elemento >0:
      contador += 1
  return contador

tabla = [-1, 2, -5, 5, 3, -8, 7, 4]

total = numeros_positivos(tabla)

print(f"El total de números positivos son: {total}")
