"""
Fatorial na Matemática
O fatorial é uma operação matemática, representada pelo símbolo de exclamação: !

A fórmula de fatorial de um número n é:
n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
"""

numero = int(input("Digite um número que deseja calcular o Fatorial: "))

resultado = 1
count = 1

while count <= numero:
    resultado_v = resultado
    resultado *= count
    print(resultado_v, " * ", count, " = ", resultado)
    count += 1

print(f"O Fatorial de {numero} é: {resultado}".format(numero, resultado))
