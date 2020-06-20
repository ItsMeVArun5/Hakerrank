#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def checkSum(arr, new_element):
    count = 0
    for num in arr:
        if ((num+new_element) % k != 0):
            count += 1
        else:
            return False

    if count == len(arr):
        return True


def nonDivisibleSubset(k, s):
    # Write your code here
    # s.sort()
    result = []
    length_of_combinations = []
    idx = 0

    for num in s:
        result = []
        result.append(num)

        for index in range(len(s)):
            if index == idx:
                continue

            # print(checkSum(result, s[index]))
            if (checkSum(result, s[index])):
                result.append(s[index])

        idx += 1
        length_of_combinations.append(len(result))
        print(result)

    return max(length_of_combinations)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
