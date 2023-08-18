import math, sys

input = sys.stdin.readline

MAX = 1000
prime = [True for i in range(MAX+1)]

prime[1] = False
for i in range (2, int(math.sqrt(MAX))+1):
    if(prime[i] == True):
        j = 2
        while i*j <= MAX:
            prime[i*j] = False
            j += 1

cnt = 0
N = int(input())
n = list(map(int, sys.stdin.readline().split()))
    
while N > 0:
    temp = n[N-1]
    
    if prime[temp]:
        cnt += 1
        
    N -= 1
print(cnt)
