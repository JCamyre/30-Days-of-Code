#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    # Sadly the Python 3 version Hackerrank wasn't updated enough for f strings.
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n*i))