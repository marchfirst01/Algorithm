number = 10000
prime = [True]*(number+1)

#배열 초기화
for i in range(1, number+1):
    prime[i] = i


for i in range (2, number):
    #i번째 배열이 0인지 확인, 이미 지워진 수라면 건너뛰기
    if(prime[i]==0): continue

    #1~number 범위에서 배수부터 출발하여 가능한 모든 숫자 지우기
    for j in range(2, number):
        j = i*j
        if(j > number): continue
        prime[j] = 0;

for i in range(2, number):
    if(prime[i] != 0): print(prime[i])
