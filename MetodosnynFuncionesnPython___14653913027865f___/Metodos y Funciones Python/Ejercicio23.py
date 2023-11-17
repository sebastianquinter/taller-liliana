"""Realizar un algoritmo que lea el archivo agenda e imprima los registros de toda
la agenda"""

def imprimir_agenda():
    archivo_agenda = "Agenda.txt"
    try:
        with open(archivo_agenda, "r") as f:
            for linea in f:
                campos = linea.strip().split(",")
                nombre_direccion = campos[0]
                ciudad = campos[1]
                codigo = campos[2]
                postal = campos[3]
                telefono = campos[4]
                edad = campos[5]
                
                print("Nombre dirección:", nombre_direccion)
                print("Ciudad:", ciudad)
                print("Código:", codigo)
                print("Código postal:", postal)
                print("Teléfono:", telefono)
                print("Edad:", edad)
                print("-" * 30)
    except FileNotFoundError:
        print("El archivo Agenda.txt no existe.")

imprimir_agenda()
