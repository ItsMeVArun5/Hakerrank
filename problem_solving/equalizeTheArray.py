#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.


def equalizeArray(arr):
    element_count = {}
    max_occurance_number = None

    for num in arr:
        element_count[num] = arr.count(num)

    max_occurance_number = max(element_count, key=element_count.get)
    return (len(arr) - arr.count(max_occurance_number))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
