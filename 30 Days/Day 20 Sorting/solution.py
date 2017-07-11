#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwapsTotal = 0
for i in range(0, n):
    numSwapsNow = 0
    for j in range(0, (n - 1)):
        if a[j] > a[j + 1]:
            numSwapsNow += 1
            a[j], a[j + 1] = a[j + 1], a[j]

    if numSwapsNow == 0:
        break
    else:
        numSwapsTotal += numSwapsNow

print("Array is sorted in " + str(numSwapsTotal) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))