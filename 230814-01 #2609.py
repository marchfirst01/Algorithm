def GCD(a, b):
    GCD = 1
    LCM = 1
    n = 2
    
    while n <= a:
        if a%n == 0 and b%n == 0:
            a = a//n
            b = b//n
            GCD *= n
            continue
        n += 1
        
    LCM = GCD * a * b
    print(GCD)
    print(LCM)
        

a, b = map(int, input().split())
if a > b:
    a, b = b, a
    
GCD(a,b)
