"""
    Escribir una función Salario que calcula los salarios de un trabajados para un numero dado 
    de horas trabajadas y un salario hora. Las horas que superan las 40 horas semanales se pagaran 
    como extras con un salario hora 1,5 veces el salario ordinario.
"""

def salario(horas_trabajadas, salario_hora):
    if horas_trabajadas > 40:
        horas_normales = 40
        horas_extra = horas_trabajadas - 40
        salario_total = (horas_normales * salario_hora) + (horas_extra * 1.5 * salario_hora)
        print("Usted superó las 40 horas, se le pagarán horas extra")
    else:
        salario_total = horas_trabajadas * salario_hora
        print("Usted no superó las 40 horas, no se le pagarán horas extra")
    return salario_total

horas_trabajadas = float(input('Ingrese las horas trabajadas: '))
salario_hora = float(input('Ingrese el valor por hora: '))

total = salario(horas_trabajadas, salario_hora)

print(f"El total es: {total}")