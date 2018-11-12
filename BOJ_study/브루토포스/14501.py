n = int(input())
t = [0 for i in range(n)]
p = [0 for i in range(n)]
ans = []
for i in range(n):
    t[i], p[i] = list(map(int, input().split() ))

def sol(idx, total):
    if idx == n:
        ans.append(total)
        return
    sol(idx+1,total)
    if idx+t[idx] <= n:
        sol(idx+t[idx],total+p[idx])

sol(0,0)
print(max(ans))