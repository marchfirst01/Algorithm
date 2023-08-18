dwarf = []
sum = 0

for i in range(9):
    n = int(input())
    sum += n
    dwarf.append(n)
dwarf.sort()

diff = sum - 100

for i in dwarf:
    if (diff-i) in dwarf and (diff-i) != i:
        dwarf.remove(i)
        dwarf.remove(diff-i)
        break
        
for i in range(7):
    print(dwarf[i])
