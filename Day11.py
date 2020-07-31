#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    sums = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for y in range(4):
        for x in range(4):
            hourglass_sum = sum(arr[y][x:x+3]) + arr[y+1][x+1] + sum(arr[y+2][x:x+3])
            sums.append(hourglass_sum)
    print(max(sums))
