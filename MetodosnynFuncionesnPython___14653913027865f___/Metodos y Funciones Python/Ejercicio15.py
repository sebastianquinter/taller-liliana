"""calcular la suma de los elementos de la diagonal principal de una matriz de 4x4"""

def suma_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

matriz = [
    [3, 0, 0, 0],
    [0, 5, 0, 0],
    [0, 0, 9, 0],
    [0, 0, 0, 2]
]

suma_diagonal = suma_diagonal_principal(matriz)
print(f"La suma de los elementos en la diagonal principal es: {suma_diagonal}")
