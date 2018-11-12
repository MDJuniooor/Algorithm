class Solution:
    def solution(self, n):
        num = []
        while n // 4 > 0:
            remains = n % 4
            n = n // 4
            num.append(remains)
        num.append(n)
        ans = sum(num)
        if ans % 2:
            return 'SS'
        else:
            return 'HS'

s = Solution()
print(s.solution(99999999999999))