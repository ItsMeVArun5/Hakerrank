#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
   arr.sort()
   maximum = sum(arr) - arr[0]
   minimum = sum(arr) - arr[4]

   print(minimum, maximum)

if __name__ == '__main__':
   arr = list(map(int, input().rstrip().split()))
   miniMaxSum(arr)
