t = int(input())
sum = 0

for i in range (t):
    n = int(input())
    for j in range(1, n+1):
        sum += n//j
    print(sum)
