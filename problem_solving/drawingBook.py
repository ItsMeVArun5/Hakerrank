#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#


def pageCount(n, p):
    half_page = n/2

    if p <= half_page:
        # start turning pages from front.
        fpage_on_left = 0
        fpage_on_right = 1
        for page_turned in range(0, n):

            if p in range(fpage_on_left, fpage_on_right+1):
                return page_turned
            else:
                fpage_on_left += 2
                fpage_on_right += 2

    else:
        # start turning pages from back.
        if n % 2 == 0:
            lpage_on_left = n
            lpage_on_right = n+1
        else:
            lpage_on_right = n
            lpage_on_left = n-1

        for page_turned in range(0, n):

            if p in range(lpage_on_left, lpage_on_right+1):
                return page_turned
            else:
                lpage_on_left -= 2
                lpage_on_right -= 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
