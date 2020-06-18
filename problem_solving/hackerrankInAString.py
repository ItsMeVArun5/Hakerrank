#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.


def hackerrankInString(s):
    seq = "hackerrank"
    seq_index = 0
    result = ""

    for letter in s:
        if seq_index == len(seq):
            break
        if letter in seq[seq_index]:
            seq_index += 1
            result += letter

    if result == seq:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
