#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    sea_level = 0
    valley_count = 0
    current_position = sea_level

    for step in s:
        if step == "U":
            current_position += 1
        else:
            current_position -= 1
            if current_position == -1:
                valley_count += 1

    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
