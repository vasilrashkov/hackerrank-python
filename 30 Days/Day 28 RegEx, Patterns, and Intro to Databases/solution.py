#!/bin/python3

import sys
import re

N = int(input().strip())
names = list()
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if bool(re.search("@gmail\.com", emailID)) :
        names.append(firstName)
        
print(*sorted(names, key=str.lower), sep='\n')

