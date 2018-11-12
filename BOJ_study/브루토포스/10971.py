from itertools import permutations
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = []

for case in permutations(range(1,n)):
    temp = a[0][case[0]]
    for i in range(len(case)-1):
        if a[0][case[0]] and a[case[i]][case[i+1]]:
            temp += a[case[i]][case[i+1]]
        else:
            temp = 0
            break
    
    if temp:
        if a[case[len(case)-1]][0]:
            temp += a[case[len(case)-1]][0]
            ans.append(temp)
print(min(ans))
