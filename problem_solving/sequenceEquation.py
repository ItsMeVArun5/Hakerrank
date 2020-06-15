#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.


def permutationEquation(p):
    result = ""

    for x in range(1, len(p)+1):
        position = p.index(x) + 1
        found = p.index(position) + 1

        result += str(found) + "\n"

    return result.rstrip("\n")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write(result)
    fptr.write('\n')

    fptr.close()
