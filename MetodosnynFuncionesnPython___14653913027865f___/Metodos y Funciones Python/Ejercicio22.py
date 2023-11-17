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

def crear_agenda():
    archivo_agenda = "Agenda.txt"
    agenda = cargar_agenda(archivo_agenda)

    while True:
        nombre_direccion = input("Ingrese el nombre de la dirección: ")
        cuidad = input("Ingrese el nombre de la ciudad: ")
        codigo = input("Ingrese el código: ")
        postal = input("Ingrese el código postal: ")
        telefono = input("Ingrese el número de teléfono: ")
        edad = input("Ingrese su edad: ")

        registro = {
            "nombre dirección": nombre_direccion,
            "ciudad": cuidad,
            "código": codigo,
            "postal": postal,
            "teléfono": telefono,
            "edad": edad
        }

        agenda.append(registro)
        guardar_agenda(agenda, archivo_agenda)  # Guarda la agenda actualizada en el archivo

        respuesta = input("¿Desea agregar otro registro? (S/N): ")
        if respuesta.upper() != "S":
            break

    print("Agenda creada:")
    for registro in agenda:
        print(registro)

crear_agenda()
