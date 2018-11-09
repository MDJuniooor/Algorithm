import sys
n,m= map(int, input().split())
read = sys.stdin.readline
poket = {}
poket2 = {}
for i in range(1,n+1):
    poket[str(i)] = read()[:-1]
    poket2[poket[str(i)]] = i

for _ in range(m):
    question = read()[:-1]
    if ord(question[0]) < 58 and ord(question[0]) > 47:
        print(poket[question])
    else:
        print(poket2[question])
