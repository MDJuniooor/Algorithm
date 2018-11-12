class Solution:
    def solution(self, o1, o2, b1, b2):
        ans = []
        for i in range(len(b1)):
            if (o1 <=b1[i] and o2 <=b2[i]) or (o1 <=b2[i] and o2 <=b1[i]):
                ans.append(b1[i]*b2[i])
        ans.sort()        
        if len(ans) == 0:
            return -1
        else:
            return ans[0]

s = Solution()
print(s.solution(17, 5, [19, 10, 12, 40], [12, 20, 15, 5]))
