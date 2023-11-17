"""diseñar una función que informa si una cadena es palíndromo
(una cadena es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda)."""

def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena_sin_espacios = cadena.replace(" ", "")
    inversa = cadena_sin_espacios[::-1]

    return cadena_sin_espacios == inversa

cadena = input("Ingrese una cadena: ")
if es_palindromo(cadena):
    print(f"{cadena} es un palíndromo.")
else:
    print(f"{cadena} no es un palíndromo.")