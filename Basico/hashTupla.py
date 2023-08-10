""" Hash de uma Tupla de inteiros
    Dado um inteiro 'n' e 'n' inteiros separados por espaço como entrada,
crie uma tupla 't' desses inteiros. Em seguida, calcule e imprima o resultado de hash(t).
  ** Nota: hash() é uma das funções do módulo __builtins__, portanto não precisa ser importado.

SOLUTION--> switch out of “Python 3” and into PyPy3 para o RackerRank!
"""


def hashTuple(n, t):
    print("Hash da linha: ", hash(t))
    hashTotal = 0
    for i in t:
        hashTotal = hashTotal + hash(i)
        print("Hash individual: ", i, "-", hash(i))

    print("Hash da soma: ", hashTotal)
    hashN = hash(n)
    # print(hashN)
    hashTotal2 = hashTotal + hashN
    print("Hash da soma 2: ", hashTotal2)

    print('The hash is:', hash(t))


if __name__ == '__main__':
    n = int(input(''))
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

    #print(hash(t), end='')

    hashTuple(n, integer_list)

