"""escribir un algoritmo que convierta los números arábigos en 
números romanos y viceversa I=1, V=5, X=10, L=50,C=100, D=500 y M=1000."""

def arabigo_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""

    i = 0
    while numero > 0:
        if numero >= valores[i]:
            resultado += simbolos[i]
            numero -= valores[i]
        else:
            i += 1

    return resultado

def romano_a_arabigo(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    prev_valor = 0

    for letra in romano[::-1]:
        valor = valores[letra]
        if valor >= prev_valor:
            resultado += valor
        else:
            resultado -= valor
        prev_valor = valor

    return resultado

numero_arabigo = 1987
numero_romano = arabigo_a_romano(numero_arabigo)
print(f"{numero_arabigo} en números romanos es: {numero_romano}")

numero_romano = "MMXXI"
numero_arabigo = romano_a_arabigo(numero_romano)
print(f"{numero_romano} en números arábigos es: {numero_arabigo}")