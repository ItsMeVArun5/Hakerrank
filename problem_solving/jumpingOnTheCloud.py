#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c, k):
    total_energy = 100
    energy_loss = 0
    current_index = 0
    current_position = c[current_index]
    remaining_energy = total_energy - energy_loss

    while True:
        current_position = c[(current_index+k) % len(c)]
        if (current_position == 1):
            energy_loss += 3
        else:
            energy_loss += 1

        if ((current_index+k) % len(c) == 0):
            break

        current_index += k

    remaining_energy = total_energy - energy_loss
    return remaining_energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
