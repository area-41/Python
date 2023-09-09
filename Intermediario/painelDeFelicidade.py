""" Painel da Felicidade
Dados 'm' e 'n', que são o tamanho do 'array' e os tamanhos de 'a' e 'b'.
Sua felicidade aumenta 1 ponto para cada valor do 'array' em 'a', e diminui
1 ponto para cada um em 'b'. Imprima o valor final da sua felicidade.
Exemplo:
        3 2   -> tamanhos
        1 5 3 -> array
        3 1   -> a
        5 7   -> b
    resposta felicidade: 1
"""


def painel(array, a, b):
    felicidade = 0
    for x in array:
        if x in a:
            felicidade += 1
        if x in b:
            felicidade -= 1
    print(felicidade)

if __name__ == '__main__':
    tamanhos = input()
    array = list(map(int, input().split()))
    a, b = set(map(int,input().split())), set(map(int, input().split()))
    painel(array, a, b)
