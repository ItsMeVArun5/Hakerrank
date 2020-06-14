#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.


def saveThePrisoner(number_of_prisoners, number_of_sweets, start):
    if ((((number_of_sweets + start - 1) % number_of_prisoners)) == 0):
        return number_of_prisoners

    return (((number_of_sweets + (start - 1)) % number_of_prisoners))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
