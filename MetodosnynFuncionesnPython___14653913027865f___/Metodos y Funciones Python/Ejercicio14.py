"""rellenar una matriz identidad de 4x 4"""

def crear_matriz_identidad(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matriz[i][i] = 1
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

dimension = 4
matriz_identidad = crear_matriz_identidad(dimension)
imprimir_matriz(matriz_identidad)