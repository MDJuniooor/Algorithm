#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
import numpy
class Solution:
    def solution(self, n):
        dp = [0 for i in range(n+1)]
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[1] = 1
        dp[2] = 2
        dp[3] = 7
        for i in range(3, n+1):
            dp[i] =1
            dp[i] = (3*dp[i-1] + dp[i-2] - dp[i-3]) % 1000000007

        return dp[n]
s=Solution()
print(s.solution(4))
