#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    # filling the k-size list with values zero.
    remainder_count = [0] * k
    count = 0

    for num in s:
        remainder_count[num % k] += 1

    for x in range(1, (k//2)+1):
        if x != k-x:
            count += max(remainder_count[x], remainder_count[k-x])

    if k % 2 == 0:
        count += 1

    count += min(remainder_count[0], 1)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
