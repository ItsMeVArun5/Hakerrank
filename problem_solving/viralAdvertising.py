#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.


def viralAdvertising(days):
    """
    Inputs:
        days  - Total number of days

    Output:
        return the cumulative number of likes at the end of the last day.
    """
    
    cumulative = 2
    day = 1
    liked = 2
    shared = 5

    day += 1

    while (day != days+1):
        shared = liked * 3
        liked = math.floor(shared/2)
        cumulative += liked
        day += 1

    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
