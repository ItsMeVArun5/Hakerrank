#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.


def beautifulDays(starting_day, ending_day, divisor):
    """
    Inputs:
        starting_day    - Starting day number
        ending_day      - Ending day number
        divisor         - Divisor

    Output:
        It returns the total number of beautiful days in the range of starting_day and ending_day.
    """

    beautiful_days = []

    for day in range(starting_day, ending_day+1):
        reverse = str(day)[::-1]
        difference = abs(int(reverse) - day)

        if (difference % divisor == 0):
            beautiful_days.append(day)

    return len(beautiful_days)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
