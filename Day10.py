#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = bin(n)[2:]
    max_consec = 0
    count = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            count += 1
        else:
            if count > max_consec:
                max_consec = count
            count = 0
    if count > max_consec:
        max_consec = count
    print(max_consec)

