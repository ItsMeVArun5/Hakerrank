#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result = []
    alice = 0
    bob = 0 
    for (x, y) in zip(a, b):
        if x>y:
            alice += 1
        elif x<y:
            bob += 1
        else:
            pass
        
    result.append(alice)
    result.append(bob)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()