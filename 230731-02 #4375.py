def n(n):
    i = 1
    num = 0
    cnt = 0
    while True:
        num = num + i
        i = i*10
        cnt += 1
        if(num%n == 0):
            break
    print(cnt)


while True:
    try:
        a = int(input())
        n(a)
    except:
        break

