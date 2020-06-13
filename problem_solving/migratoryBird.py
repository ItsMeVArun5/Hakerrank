#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.


def migratoryBirds(arr):
    result = 0
    b_type = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    for bird in arr:
        if bird == 1:
            b_type[1] += 1
        elif bird == 2:
            b_type[2] += 1
        elif bird == 3:
            b_type[3] += 1
        elif bird == 4:
            b_type[4] += 1
        else:
            b_type[5] += 1

    temp = b_type[1]

    for x in b_type:
        if b_type[x] > temp:
            temp = b_type[x]
            key = x

    return key


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
