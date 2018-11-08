class Solution:
    def solution(self, k, w):
        cnt = 0 
        dic = {}
        for i in range(len(k)):
            dic[k[i]] = i
        for i in range(1,len(w)):
            tmp1 = dic[w[i-1]]
            tmp2 = dic[w[i]]
            cnt+=abs(tmp2-tmp1)
        return cnt
