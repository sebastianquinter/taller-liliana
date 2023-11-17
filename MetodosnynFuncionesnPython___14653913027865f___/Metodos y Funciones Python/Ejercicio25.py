"""Diseñar un algoritmo que permita modificar el contenido de alguno de los
registros del archivo secuencial agenda mediante datos introducidos por
teclado."""


import unicodedata

def eliminar_acentos(cadena):
    nfkd_form = unicodedata.normalize("NFKD", cadena)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def cargar_agenda(archivo):
    agenda = []
    try:
        with open(archivo, "r") as f:
            for linea in f:
                campos = linea.strip().split(",")
                registro = {
                    "nombre dirección": campos[0],
                    "ciudad": campos[1],
                    "código": campos[2],
                    "postal": campos[3],
                    "teléfono": campos[4],
                    "edad": campos[5]
                }
                agenda.append(registro)
    except FileNotFoundError:
        print("El archivo Agenda.txt no existe.")
    return agenda

def guardar_agenda(agenda, archivo):
    with open(archivo, "w") as f:
        for registro in agenda:
            linea = f"{registro['nombre dirección']},{registro['ciudad']},{registro['código']},{registro['postal']},{registro['teléfono']},{registro['edad']}\n"
            f.write(linea)

def modificar_registro(agenda):
    indice = int(input("Ingrese el número de registro a modificar: ")) - 1
    if 0 <= indice < len(agenda):
        registro = agenda[indice]
        print("Registro actual:")
        for campo, valor in registro.items():
            print(f"{campo}: {valor}")
        
        campo_modificar = eliminar_acentos(input("Ingrese el campo a modificar: ").lower())
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo_modificar}: ")
        
        if campo_modificar in registro:
            registro[campo_modificar] = nuevo_valor
            print("Registro modificado.")
        else:
            print("Campo inválido.")
    else:
        print("Índice inválido.")

archivo_agenda = "Agenda.txt"
agenda = cargar_agenda(archivo_agenda)
for i, registro in enumerate(agenda, start=1):
    print(f"{i}. {registro['nombre dirección']} - {registro['teléfono']}")

modificar_registro(agenda)
guardar_agenda(agenda, archivo_agenda)
