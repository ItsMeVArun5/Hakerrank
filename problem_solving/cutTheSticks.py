#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(sticks):
    result = []

    while len(sticks) >= 1:
        result.append(len(sticks))

        small_stick = min(sticks)
        number_of_small_sticks = sticks.count(small_stick)

        for x in range(number_of_small_sticks):
            sticks.remove(small_stick)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
