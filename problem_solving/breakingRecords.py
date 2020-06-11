#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.


def breakingRecords(scores):
    s_min = scores[0]
    s_max = scores[0]

    breaking_least_point = 0
    breaking_max_point = 0

    result = []

    for score in scores:
        if score > s_max:
            s_max = score
            breaking_max_point += 1

        if score < s_min:
            s_min = score
            breaking_least_point += 1

    result.append(breaking_max_point)
    result.append(breaking_least_point)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
