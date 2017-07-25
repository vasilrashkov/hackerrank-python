from math import sqrt

T = int(input())

def is_prime(num):
    if num == 1:
        return False
    i=2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True

for i in range(T):
    number = int(input())
    isPrime = is_prime(number)
    if isPrime:
        print("Prime")
    else :
        print("Not prime")