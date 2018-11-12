n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
dp = [0]*(n+1)
dp[1] = a[1]
if n > 1:
    for i in range(2, n+1):
        temp = []
        for j in range(1, n+1):
            if i-j >= 0:
                temp.append(dp[i-j]+a[j])
        dp[i] = min(temp)

print(dp[n])
