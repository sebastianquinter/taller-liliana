"""dado el nombre de una serie de estudiantes y las calificaciones 
obtenidas en un examen, calcular e imprimir la calificación media 
así como cada calificación y la diferencia con la media."""

def calcular_media(calificaciones):
    total_calificaciones = sum(calificaciones)
    media = total_calificaciones / len(calificaciones)
    return media

def imprimir_calificaciones_con_diferencia(nombres, calificaciones, media):
    print("Calificaciones individuales y diferencia con la media:")
    for nombre, calificacion in zip(nombres, calificaciones):
        diferencia = calificacion - media
        print(f"{nombre}: Calificación = {calificacion}, Diferencia = {diferencia:.2f}")

num_estudiantes = int(input("Ingrese el número de estudiantes: "))

nombres = []
calificaciones = []

for i in range(num_estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
    nombres.append(nombre)
    calificaciones.append(calificacion)

media = calcular_media(calificaciones)
print(f"La calificación media es: {media:.2f}")

imprimir_calificaciones_con_diferencia(nombres, calificaciones, media)