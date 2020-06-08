#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
   r = int(n)
   for x in range(1,n+1):
      space = r-x
      print(" " * space + "#" * x)

if __name__ == '__main__':
   n = int(input())

   staircase(n)

