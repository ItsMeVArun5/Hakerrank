#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    jumping = True
    jumps = 0
    meeting_at_one_point = False

    while jumping:
        jumps += 1
        if jumps > 10000:
            break

        x1 += v1
        x2 += v2
        if x1 == x2:
            meeting_at_one_point = True
            break

    if meeting_at_one_point:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + "\n")

    fptr.close()
