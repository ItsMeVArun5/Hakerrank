#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    cost = []
    # Making all 8 possible combination of magic square matrix.
    first_matrix = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9 ,2],
    ]

    second_matrix = [
        [6, 1, 8],
        [7, 5, 3],
        [2, 9 ,4],
    ]

    third_matrix = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1 ,6],
    ]

    fourth_matrix = [
        [2, 9, 4],
        [7, 5, 3],
        [6, 1 ,8],
    ]

    fifth_matrix = [
        [8, 3, 4],
        [1, 5, 9],
        [6, 7 ,2],
    ]

    sixth_matrix = [
        [4, 3, 8],
        [9, 5, 1],
        [2, 7 ,6],
    ]

    seventh_matrix = [
        [6, 7, 2],
        [1, 5, 9],
        [8, 3 ,4],
    ]

    eith_matrix = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3 ,8],
    ]

    all_magic_matrix = [first_matrix, second_matrix, third_matrix, fourth_matrix,                               fifth_matrix, sixth_matrix, seventh_matrix, eith_matrix]

    # Computing sum of elements of 3 row of given 3x3 matrix.
    row1 = [s[0][0], s[0][1], s[0][2]]
    row2 = [s[1][0], s[1][1], s[1][2]]
    row3 = [s[2][0], s[2][1], s[2][2]]

    sum_row1 = sum(row1)
    sum_row2 = sum(row2)
    sum_row3 = sum(row3)
    
    sum_of_rows = [sum_row1, sum_row2, sum_row3]
    matrix_sum = []
    index = 0
    rsum = 0


    # Computing cost.
    for magic_matrix in all_magic_matrix:
        index = -1
        rsum = 0

        for row in magic_matrix:
            index += 1

            for x,y in zip(row, s[index]):
                rsum += abs(x-y)

        matrix_sum.append(rsum)            

    return min(matrix_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
