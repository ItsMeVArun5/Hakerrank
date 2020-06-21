#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    current_position = 0
    next_position = 0
    step_count = 0
    max_jump = 2

    while (current_position != (len(c)-1)):
        next_position = current_position + max_jump

        if (next_position > len(c)-1):
            current_position += 1
            step_count += 1
            continue

        if (c[next_position] == 1):
            current_position += 1
            step_count += 1
        else:
            current_position += 2
            step_count += 1

    return step_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
