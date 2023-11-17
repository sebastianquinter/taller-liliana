"""diseñar un algoritmo de una fusión que convierta una cadena en mayúscula y otra que la convierta minúscula."""

def mayuscula_minuscula(cadena):
  cadena_mayuscula = cadena.upper()
  cadena_minuscula = cadena.lower()
  return cadena_mayuscula, cadena_minuscula

cadena = input("Ingrese una cadena (Palabra o frase): ")
mayuscula, minuscula = mayuscula_minuscula(cadena)
print(f"El resultado de la frase en mayuscula es: {mayuscula}")
print(f"El resultado de la frase en minuscula es: {minuscula}")
