#!/bin/python3

import numpy as np


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
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

    return abs(d1 - d2)


if __name__ == '__main__':

    n = np.random.randint(10, size=(1))
    print(n)
    arr = np.random.randint(10, size=(int(n), int(n)))
    print(arr)

    result = diagonalDifference(arr)
    print(result)