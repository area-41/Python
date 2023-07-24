""" Entre 2 sets
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
    The elements of the first array are all factors of the integer being considered
    The integer being considered is a factor of all elements of the second array

    Function Description
Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
    getTotalX has the following parameter(s):
        int a[n]: an array of integers
        int b[m]: an array of integers
    Returns
        int: the number of integers that are between the sets
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

        [2, 3] [2, 4] [16, 32, 96] <--- para este input
        2 e 4 dividem-se igualmente em 4, 8, 12 e 16.
        4, 8 e 16 dividem-se igualmente em 16, 32, 96.
    4, 8 e 16 são os únicos três números para os quais cada elemento de a é um fator e cada um
    é um fator de todos os elementos de b.
"""


def getTotalX(arr, brr):
    list_numbers_a = []
    max_a = number = max(arr)  # estipular numero eplo max da lista a
    min_b = min(brr)
    while max_a <= number <= min_b:  # correr a lista de n entre os setes
        a_list = []
        for a in arr:  # percorrer cada elemento do array
            if number % a == 0:
                a_list.append(1)
                b_list = []
                for b in brr:
                    if b % number == 0:
                        b_list.append(1)
            if len(a_list) == len(arr):  # verificar se o tamanho de cada lista é igual
                if len(b_list) == len(brr):  # tamanho iguais = fatoral de todos
                    if number not in list_numbers_a:
                        list_numbers_a.append(number)
        number += 1
    print(list_numbers_a)
    return len(list_numbers_a)


if __name__ == '__main__':
    print(getTotalX([2, 4], [16, 32, 96]))
    print(getTotalX([3, 4], [24, 48]))
    # total = getTotalX(arr, brr)
    # print(total)
