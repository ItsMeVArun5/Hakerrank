#!/bin/python3

import math
import os
import random
import re
import sys


# Calculating slope.
def getSlope(x1, y1, x2, y2):
    if ((y2 - y1) == 0 or (x2 - x1) == 0):
        return 0

    return (y2 - y1)//(x2 - x1)


# Calculating distance.
def getDistance(x1, y1, x2, y2):
    # dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # return int(dist)
    return max(abs(x1 - x2), abs(y1 - y2))


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    print(obstacles, len(obstacles))
    queenX = c_q
    queenY = r_q

    if k == 0 and n == 1:
        return 0

    diagonal_up_left = []
    diagonal_up_right = []
    diagonal_bot_right = []
    diagonal_bot_left = []

    vertical_up = []
    vertical_bot = []
    horizontal_left = []
    horizontal_right = []

    for x, y in obstacles:
        slope = getSlope(x, y, r_q, c_q)
        # print(slope)

        # Checking for diagonal obstacle and its direction.
        if (slope == 1 and (x+y) > (r_q+c_q)):
            distance = getDistance(x, y, r_q, c_q) - 1
            diagonal_up_right.append(distance)
        elif (slope == 1 and (x+y) < (r_q+c_q)):
            distance = getDistance(x, y, r_q, c_q) - 1
            diagonal_bot_left.append(distance)
        elif (slope == -1 and x > r_q):
            distance = getDistance(x, y, r_q, c_q) - 1
            diagonal_up_left.append(distance)
        elif (slope == -1 and x < r_q):
            distance = getDistance(x, y, r_q, c_q) - 1
            diagonal_bot_right.append(distance)
        else:
            pass

        # Checking for vertical obstacle and its direction.
        if (y == c_q and x > r_q):
            distance = getDistance(x, y, r_q, c_q) - 1
            # if distance == 1:
            #     vertical_up.append(0)
            # else:
            vertical_up.append(distance)
        elif (y == c_q and x < r_q):
            distance = getDistance(x, y, r_q, c_q) - 1
            # if distance == 1:
            #     vertical_bot.append(0)
            # else:
            vertical_bot.append(distance)
        else:
            pass

        # Checking for horizontal obstacle and its direction.
        if (slope == 0 and (x+y) > (r_q+c_q) and x == r_q):
            distance = getDistance(x, y, r_q, c_q) - 1
            # if distance == 1:
            #     horizontal_right.append(0)
            # else:
            horizontal_right.append(distance)
        elif (slope == 0 and (x+y) < (r_q+c_q) and x == r_q):
            distance = getDistance(x, y, r_q, c_q) - 1
            # if distance == 1:
            #     horizontal_left.append(0)
            # else:
            horizontal_left.append(distance)
        else:
            pass

    if(diagonal_up_right == []):
        diagonal_up_right.append(n - max([r_q, c_q]))

    if(diagonal_bot_left == []):
        diagonal_bot_left.append(min([r_q, c_q])-1)

    if (diagonal_bot_right == []):
        if (r_q == 1 and c_q == 1):
            diagonal_bot_right.append(0)
        else:

            diagonal_bot_right.append(min(n-c_q, r_q-1))
            # bx = abs(n - sum([r_q, c_q]))
            # diagonal_bot_right.append(abs(bx - r_q))

    if (diagonal_up_left == []):
        if (r_q == 1 and c_q == 1):
            diagonal_up_left.append(0)
        else:
            diagonal_up_left.append(min(c_q-1, n-r_q))
            # uy = abs(n - sum([r_q, c_q]))
            # ux =  sum([r_q, c_q]) - uy
            # diagonal_up_left.append(abs(ux - r_q))

    if (horizontal_right == []):
        horizontal_right.append(n - c_q)

    if (horizontal_left == []):
        horizontal_left.append(c_q - 1)

    if (vertical_up == []):
        vertical_up.append(n - r_q)

    if (vertical_bot == []):
        vertical_bot.append(r_q - 1)

    print("DUR: ", diagonal_up_right, "DBL: ", diagonal_bot_left,
          "DUL: ", diagonal_up_left, "DBR: ", diagonal_bot_right)
    print("VU: ", vertical_up, "VB: ", vertical_bot)
    print(horizontal_left, horizontal_right)

    return min(diagonal_bot_left) + min(diagonal_bot_right) + min(diagonal_up_left) + min(diagonal_up_right) + min(vertical_bot) + min(vertical_up) + min(horizontal_left) + min(horizontal_right)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
