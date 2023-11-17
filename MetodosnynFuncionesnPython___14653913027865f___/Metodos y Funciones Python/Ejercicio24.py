"""Diseñar un algoritmo que cope el archivo secuencial agenda de los ejercicios
anteriores en un archivo directo directo_agenda, de modo que cada registro
mantenga su posición relativa."""


def copiar_agenda():
    archivo_origen = "Agenda.txt"
    archivo_destino = "directo_agenda.txt"
    
    try:
        with open(archivo_origen, "r") as origen, open(archivo_destino, "w") as destino:
            for linea in origen:
                destino.write(linea)
                
        print("Contenido de la agenda copiado exitosamente.")
    except FileNotFoundError:
        print("El archivo Agenda.txt no existe.")

copiar_agenda()
