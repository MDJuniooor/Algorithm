import sys
sys.setrecursionlimit(100000)
cnt=[0,0]

def permfunc(i,j,perm,count):
    ary = perm[:]
    ary[i],ary[j] = ary[j],ary[i]
    print(ary,count)
    check=False
    for i in range(len(ary)):
        for j in range(i, len(ary)):
            if ary[i] > ary[j]:
                permfunc(i, j, ary, count+1)
                check=True
    if check==False:
        cnt[0]+=1
        cnt[1]+=count

class Solution:
    def solution(self, perm):
        check=True
        for i in range(len(perm)):
            for j in range(i, len(perm)):
                if perm[i]>perm[j]:        
                    check=False
                    permfunc(i, j, perm, 1)
        
        if check:
            print(0)
        else:
            print(cnt[0], cnt[1], cnt[1]/cnt[0])



Solution().solution([1,3,2,4])
