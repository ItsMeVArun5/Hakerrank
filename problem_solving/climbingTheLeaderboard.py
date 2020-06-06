#!/bin/python3

import math
import os
import random
import re
import sys

def binarySearch (arr, lb, ub, x): 
  
    # Check base case 
    if ub >= lb: 
  
        mid = lb + (ub - lb) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid+1 

        # If the array length is one.
        elif len(arr)==1:
            return mid

        # If element is smaller than mid, then it  
        # can only be present in right subarray 
        elif arr[mid] > x:
            return binarySearch(arr, mid+1, ub, x) 
  
        # Else the element can only be present  
        # in left subarray 
        else: 
            return binarySearch(arr, lb, mid-1, x) 
  
    else: 
        return lb+1

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    non_Repeated_scores = []
    ranking = []
    count = 0

    # Removing duplicates from leaderboard.
    # Used dictonaries to decerase time complexity.
    non_Repeated_scores = list(dict.fromkeys(scores)) 

    for x in alice:
        ranking.append(binarySearch(non_Repeated_scores, 0, len(non_Repeated_scores)-1, x))
            
    return ranking


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
