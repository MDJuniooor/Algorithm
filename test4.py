from collections import defaultdict
class Solution:
    def solution(self, A):
        cnt = 1
        while cnt<=len(A):
            L = []
            for i in range(0,len(A)-cnt+1):
                seq = [A[i]]
                for j in range(i+1,i+cnt):
                    seq.append(A[j])
                L.append(tuple(seq))         
            if len(L) == 1:
                return cnt
            else:
                dic = defaultdict(lambda : None)
                check = True
                for i in range(0, len(A)-cnt+1):
                    key = L[i]
                    if i + cnt < len(A):
                        if dic[key] != None and dic[key] != A[i+cnt]:
                            check = False
                        else:
                            dic[key] = A[i+cnt]
                if check:
                    return cnt
            cnt+=1      
        return cnt

s=Solution()
print(s.solution([1,2,3,4,1,2,3,5]))