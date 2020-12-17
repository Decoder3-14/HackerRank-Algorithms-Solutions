#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifferenceEnhanced(arr):
    n = len(arr)
    
    leftToRight = 0
    rightToLeft = 0
    for i in range(0, n):
        leftToRight += arr[i][i]
        rightToLeft += arr[i][n - i - 1]
    return abs(leftToRight - rightToLeft)


def diagonalDifference(arr):
    n = len(arr)
    
    leftToRight = 0
    rightToLeft = 0
    
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                leftToRight += arr[i][j]
            if ((i + j) == (n - 1)): 
                rightToLeft += arr[i][j] 
                
    return abs(leftToRight - rightToLeft)
    
                
    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
