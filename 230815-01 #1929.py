import math

MAX = 1000000
prime = [True for i in range(MAX+1)]

prime[1] = False
for i in range (2, int(math.sqrt(MAX))+1):
    if(prime[i] == True):
        j = 2
        while i*j <= MAX:
            prime[i*j] = False
            j += 1

M, N = map(int, input().split())

for i in range(M, N+1):
    if(prime[i]): print(i)
