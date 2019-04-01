#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    i = abs(z - x)
    j = abs(z - y)
    if (i == j):
        print("Mouse C")
    elif ( i < j):
        print("Cat A")
    elif ( i > j):
        print("Cat B")

 
if __name__ == '__main__':

    q = int(input())
   
    for _ in range(q):
        x = int(input())

        y = int(input())

        z = int(input())

    catAndMouse(x, y, z)

    

    
