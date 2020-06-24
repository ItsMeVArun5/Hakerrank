#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.


def minimumDistances(arr):
    print(arr, "size: ", len(arr))
    distance = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] == arr[j]):
                distance.append(j-i)

    print(distance)
    if distance == []:
        return -1
    else:
        return min(distance)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
