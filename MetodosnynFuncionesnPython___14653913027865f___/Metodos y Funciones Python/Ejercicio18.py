"""escribir un algoritmo para contar el numero de ocurrencias de 
cada una de las palabras ‘a’, ‘an’,’and’ en las diferentes líneas de texto."""

def contar_ocurrencias(texto, palabras):
    ocurrencias = {palabra: 0 for palabra in palabras}
    lineas = texto.split("\n")

    for linea in lineas:
        palabras_linea = linea.split()
        for palabra in palabras_linea:
            if palabra in ocurrencias:
                ocurrencias[palabra] += 1

    return ocurrencias

texto = """
This is an example text.
An apple and an orange are on the table.
The cat is sleeping.
"""

palabras_a_contar = ['a', 'an', 'and']

resultados = contar_ocurrencias(texto, palabras_a_contar)

for palabra, ocurrencias in resultados.items():
    print(f"'{palabra}' aparece {ocurrencias} veces.")
