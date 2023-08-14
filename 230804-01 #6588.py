import math, sys

input = sys.stdin.readline

number = 1000000
prime = [True for i in range(number+1)]

prime[1] = 0

for i in range (2, int(math.sqrt(number))+1):
    if(prime[i] == True):
        j = 2
        while i*j <= number:
            prime[i*j] = False
            j += 1

while(True):
    hasGold = False
    n = int(input().rstrip())

    if n < 6 or n > number or n == 0:
        break
    
    for i in range(3, number+1, 2):
        if(prime[i] and prime[n - i]):
            hasGold = True
            print(n, "=", i, "+", n-i)
            break

    if not hasGold:
        print("Goldbach's conjecture is wrong.")
        break
