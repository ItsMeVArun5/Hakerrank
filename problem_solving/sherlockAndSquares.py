#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.


def squares(lower_bound, upper_bound):
    in_range = []
    count = 0
    square = []

    for num in range(1, upper_bound+1):
        if num**2 > upper_bound:
            break
        else:
            square.append(num**2)

    for num in square:
        if num in range(lower_bound, upper_bound+1):
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
