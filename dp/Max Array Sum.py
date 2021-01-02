#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.


def maxSubsetSum(arr):
    kip, kipn = 0, 0
    i = 0
    for elem in arr:
        i = i + 1
        print('Iter #', i)
        print('{excl', kipn, ', incl', kip, '}')
        nexc = max(kip, kipn)
        kip = kipn + elem
        kipn = nexc
        print('{excl', kipn, ', incl', kip, '}')
        print('---------------')
    return max(kip, kipn)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
