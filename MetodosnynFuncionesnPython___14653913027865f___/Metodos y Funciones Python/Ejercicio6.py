"""Diseñar un procedimiento que acepte un numero de mes, un numero de día y
 un numero de año y los visualice en el formato dd/mm/aa Por ejemplo, los valores
   19,09,1987 se visualizarían así: 19/9/87 y para los valores 3,9, y 1905 así: 3/9/05."""

def visualizar_fecha(dia, mes, anio):
    mes_str = str(mes)
    dia_str = str(dia)
    anio_str = str(anio)[-2:]

    fecha_formateada = f"{dia_str}/{mes_str}/{anio_str}"
    print(fecha_formateada)

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

visualizar_fecha(dia, mes, anio)

