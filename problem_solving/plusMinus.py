#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    positive_elements = 0
    negative_elements = 0
    zero_elements = 0

    for x in arr:
        if x > 0:
            positive_elements += 1
        elif x == 0:
            zero_elements += 1
        else:
            negative_elements += 1

    print("{0:.6f}".format(positive_elements / len(arr), 6))
    print("{0:.6f}".format(negative_elements / len(arr), 6))
    print("{0:.6f}".format(zero_elements / len(arr), 6))


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
