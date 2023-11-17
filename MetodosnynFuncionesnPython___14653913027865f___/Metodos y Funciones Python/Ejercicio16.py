"""diseñar un algoritmo que calcule el mayor valor de una lista L de N elementos"""

def encontrar_mayor_valor(lista):
    if not lista:
        return None

    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return mayor

lista = [9, 4, 12, 7, 15, 2, 10]

mayor_valor = encontrar_mayor_valor(lista)
if mayor_valor is not None:
    print(f"El mayor valor en la lista es: {mayor_valor}")
else:
    print("La lista está vacía.")
