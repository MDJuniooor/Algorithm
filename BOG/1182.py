n,s = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
cnt = [0]
def Sum(cIdx, cSum,chosen):
    if(cIdx == n):
        if cSum == s and chosen:
            cnt[0]+=1
        return
    Sum(cIdx+1,cSum+L[cIdx],1)
    Sum(cIdx+1,cSum,chosen)

Sum(0,0,0)

print(cnt[0])

