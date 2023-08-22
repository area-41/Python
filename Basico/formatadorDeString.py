""" Formatador de String para Decimal, Octal, Hexadecimal, Binário
Dado um inteiro, imprima os seguintes valores para cada inteiro de 1 a n:
    Decimal, Octal, Hexadecimal (em letras maiúsculas) e Binário.
Descrição da função
    Conclua a função print_formatted, que tem os seguintes parâmetros:
    número int: o valor máximo para imprimir
Impressões
    Os quatro valores devem ser impressos em uma única linha na ordem especificada acima para cada i
    de 1 ao número n. Cada valor deve ser preenchido com espaço para corresponder à largura do valor binário de
    e os valores devem ser separados por um único espaço.
Formato de entrada
    Um único inteiro denotando n.
Restrições
    1<=n<=99
Exemplo de entrada
    17
Saída de amostra
    ...
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   ...
"""


def print_formatted(number):
    len_bin = len(f"{number:b}")  # converter o número : binário para uma string e pegando o seu tamanho
    for i in range(1, number+1):
        print(str(i).rjust(len_bin),  # converter o decimal para string
              oct(i)[2:].rjust(len_bin),  # cortar para exibir a partir do 2 caracter
              hex(i).upper()[2:].rjust(len_bin),
              bin(i)[2:].rjust(len_bin))

    print("-"*60)
    # versão mais compacta mais avançada usando comandos nativos do Python
    for i in range(1, number + 1):
        print(f"{i:{len_bin}d} {i:{len_bin}o} {i:{len_bin}X} {i:{len_bin}b}")


if __name__ == '__main__':
    # n = int(input())
    n = 17
    print_formatted(n)
