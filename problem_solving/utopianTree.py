#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    tree_height = 1
    height = {
        "spring": 2,
        "summer": 1
        }
    
    wheather = "spring"
    
    while(n!=0):
        if wheather=="spring":
            tree_height *= height["spring"]
            wheather = "summer"
            n -= 1
        else:
            tree_height += height["summer"]
            wheather = "spring"
            n -= 1

    return tree_height
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
