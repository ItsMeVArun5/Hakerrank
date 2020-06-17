#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.


def appendAndDelete(initial_string, target_string, given_step):
    non_match_count = 0
    steps_required = 0
    length_of_string = len(initial_string)
    length_of_target = len(target_string)

    while (initial_string[:length_of_string] != target_string[:length_of_string]):
        length_of_string -= 1
        non_match_count += 1

    steps_required = (length_of_target - length_of_string) + non_match_count

    if given_step < steps_required:
        return "No"
    elif (len(s)+len(t)) <= given_step:
        return "Yes"
    elif 2*len(t) < given_step:
        return "Yes"
    elif given_step % 2 == steps_required % 2:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
