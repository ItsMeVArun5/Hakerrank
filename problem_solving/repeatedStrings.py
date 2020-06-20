#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    total_a_count = 0
    occurance_of_a = s.count("a")

    number_of_string_occurance = n//len(s)
    total_a_count = number_of_string_occurance * occurance_of_a
    remaining_characters = s[:n % len(s)]
    total_a_count += remaining_characters.count("a")

    return total_a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
