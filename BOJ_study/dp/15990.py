import sys
n = int(input())
dp = [0] * 100001
dp[1] = 1
dp[2] = 2
for i in range(100001):
    dp[i-3]+1
    dp[i-2]+1
    dp[i-1]+1