class Solution:
    def solution(self, maxN):
        maxN.sort()
        ans = maxN[0]
        if len(maxN) == 0:
            return 0
        if len(maxN) == 1:
            return ans
        for i in range(1,len(maxN)):
            if ans <= 0:
                ans = 0 
                break
            else:
                ans = ans * (maxN[i]-i) % 1000000007
        return ans


s= Solution()
print(s.solution([4,4,5]))
