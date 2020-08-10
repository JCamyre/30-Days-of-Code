#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0
def swap(arr, pos):
    a1 = arr[pos]
    arr[pos] = arr[pos+1]
    arr[pos+1] = a1


for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            swap(a, j)
            swaps += 1
print(rf'Array is sorted in {swaps} swaps.')
print(rf'First Element: {a[0]}')
print(rf'Last Element: {a[-1]}')
