#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1, n + 1):
        text = "#" * i
        print(text.rjust(n))

    """
    counter = 1
    while counter <= n:
        print(" "*(n-counter),"#"*counter)
        counter += 1
    """

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)