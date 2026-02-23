#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    first=s.split(" ")
    L=len(first)
    for i in range(L):
        if first[i]!="":
         if first[i][0].isalpha():
            first[i]=first[i].capitalize()
    return ' '.join(first)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
