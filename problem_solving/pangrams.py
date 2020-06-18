#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.


def pangrams(s):
    letters = []
    s = s.lower()

    for x in s:
        if x not in letters:
            letters.append(x)

    if " " in letters:
        letters.remove(" ")

    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
