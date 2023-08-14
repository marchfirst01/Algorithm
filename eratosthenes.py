import math, sys

MAX = 100
prime = [True for i in range(MAX+1)]

for i in range (2, int(math.sqrt(MAX))+1):
    if(prime[i] == True):
        j = 2
        while i*j <= MAX:
            prime[i*j] = False
            j += 1

for i in range(2, MAX):
    if(prime[i]): print(i)
