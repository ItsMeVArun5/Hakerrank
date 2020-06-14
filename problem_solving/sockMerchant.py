#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    ar.sort()
    sock = []
    pair_count = 0

    # removing duplicates and appending it to new list.
    for x in ar:
        if x not in sock:
            sock.append(x)

    # counting pair.
    for y in sock:
        pair_count += int(ar.count(y)/2)

    return str(pair_count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
