#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.


def dayOfProgrammer(year):
    leap_year = False
    month = 9
    day = 13

    # If year is 1918.
    if year == 1918:
        day += 13
        return str(day)+".0"+str(month)+"."+str(year)

    leap_year = checkLeapYear(year)

    if leap_year:
        day -= 1
        return str(day)+".0"+str(month)+"."+str(year)
    else:
        return str(day)+".0"+str(month)+"."+str(year)

# Checking leap year or not.


def checkLeapYear(year):
    isJulianCalender = False
    isGregorianCalender = False
    leap_year = False

    # Checking calender.
    if year > 1918:
        isGregorianCalender = True
    else:
        isJulianCalender = True

    # Checking wheather leap year or not according to the calender it follows.
    if isJulianCalender:
        if year % 4 == 0:
            leap_year = True
            return leap_year
        else:
            return leap_year
    else:
        if year % 400 == 0:
            leap_year = True
            return leap_year
        elif year % 4 == 0 and year % 100 != 0:
            leap_year = True
            return leap_year


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
