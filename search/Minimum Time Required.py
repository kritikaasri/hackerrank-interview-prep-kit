#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.


def minTime(machines, goal):
    totm = len(machines)
    lb = (min(machines) * goal) // totm
    ub = ((max(machines) * goal) // totm) + 1
    while lb < ub:
        days = (lb + ub) // 2
        produx = sum([(days // masheens) for masheens in machines])
        if produx < goal:
            lb = days + 1
        else:
            ub = days
    return lb


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
