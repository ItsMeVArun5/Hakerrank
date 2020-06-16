#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.


def findDigits(number):
    divisor = number
    count = 0

    while number > 0:
        digit = number % 10

        if ((digit != 0) and (divisor % digit == 0)):
            count += 1

        number //= 10

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
