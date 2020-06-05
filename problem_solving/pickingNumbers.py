#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here.
    a.sort()
    pickingNumbers = []
    individual_count = []
    num = []

    # Removing duplicates.
    for x in a:
        if x not in num:
            num.append(x)
    
    if (len(num) == 1):
        return a.count(num[0])

    for x in range(0,len(num)-1):
        individual_count.append(a.count(num[x]))
        if ((num[x+1]-num[x]<=1)):
            pickingNumbers.append(a.count(num[x])+a.count(num[x+1]))

    if (max(individual_count)>max(pickingNumbers)):
        return max(individual_count)
    else:
        return max(pickingNumbers)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
