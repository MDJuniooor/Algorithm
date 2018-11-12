import itertools
n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
for case in itertools.permutations(a,len(a)):
    temp = 0
    for i in range(len(case)-1):
        temp += abs(case[i]-case[i-1])
    ans = max(ans, temp)
print(ans)
