#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sums = []
    copy_arr = arr.copy()
    for i in range(len(arr)):
        el = copy_arr.pop(i)
        sums.append(sum(copy_arr))
        copy_arr.insert(i, el)
        
    print(min(sums), max(sums))
        
            

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
