#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = int(s[0:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])

    day = False
    night = False

    if (s[8]) == "P":
        night = True
    else:
        day = True

    if day:
        if hour == 12:
            s = s.replace(s[0:2], "00")
        s = s.replace(s[8:], "")
        return s
    else:
        if hour == 12:
            s = s.replace(s[8:], "")
            return s
        else:
            new_hour = 12 + hour
            s = s.replace(s[0:2], str(new_hour))
            s = s.replace(s[8:], "")
            return s


if __name__ == "__main__":
    f = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    f.write(result + "\n")

    f.close()
