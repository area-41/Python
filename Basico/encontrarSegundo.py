"""Encontre o Vice-Campeão
Dada uma lista ARR, encontre a pontuação máxima e imprima o vice,
 o segundo máximo.
"""

if __name__ == '__main__':
    n = 5
    arr = "2 3 6 6 5"
    arr = arr.split()  # quebrar a string dada nos espaços

    # n = int(input())  # código de input do exercício original
    # arr = map(int, input().split())

    result = []  # criar uma nova lista
    for i in arr:  # correr todos os elementos do array
        if i not in result:  # se o elemento não está na lista, adiciona
            result.append(i)
    result.sort()  # põe a lista em ordem
    result.pop()  # tira o mais alto, o campeão
    print(result[-1])  # imprime o vice
