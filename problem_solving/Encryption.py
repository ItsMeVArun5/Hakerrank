#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.


def encryption(s):
    length = len(s)
    sqr_root = math.sqrt(length)
    rows = math.floor(sqr_root)
    cols = math.ceil(sqr_root)
    grid_area = []
    characters_in_grid = []
    select_grid_area = None
    result = ""
    temp = ""

    # Removing spaces in string.
    s.replace(" ", "")
    print(s)

    # Setting up the smallest grid area.
    if (rows*cols >= length):
        grid_area.append(dict({
            "rows": rows,
            "cols": cols,
            "area": rows*cols
        }))

    elif (rows*rows >= length):
        grid_area.append(dict({
            "rows": rows,
            "cols": rows,
            "area": rows*rows
        }))
    elif (cols*cols >= length):
        grid_area.append(dict({
            "rows": cols,
            "cols": cols,
            "area": cols*cols
        }))

    select_grid_area = min(grid_area)

    # Creating new desire string.
    for initial in range(len(s)):
        result += " "
        if len(temp) == len(s):
            break

        for index in range(0, len(s), select_grid_area["cols"]):
            if (initial+index >= len(s) or len(temp) == len(s)):
                break

            result += s[initial+index]
            temp += s[initial+index]

    return result.lstrip()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
