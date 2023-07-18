import numpy as np
"""
A função aceita 2D_INTEGER_ARRAY arr como parâmetro.
A função deve retornar um INTEGER
"""


def diferencaDiagonais(arr):
    d1 = 0
    d2 = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                d1 += arr[i][j]

            if i == n - j - 1:
                d2 += arr[i][j]

            j += 1
        i += 1

    return abs(d1 - d2)  # retorna um valor absoluto


if __name__ == '__main__':
    # função random para criar uma quantidade até 10 aleatória de linhas
    n = np.random.randint(10, size=1)
    print("\nQtde de linhas: ", n)

    # função random para criar números aleatórios até 10 e preencher as linhas
    arr = np.random.randint(10, size=(int(n), int(n)))
    print("\n", arr)

    result = diferencaDiagonais(arr)
    print("\nResultado da diferença entre a soma das diagonais: \n", result)
