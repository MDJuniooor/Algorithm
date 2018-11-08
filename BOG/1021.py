D=[] 
mList=[]
pointer=0
count=0
N, M = map(int, input().split())
L = list(map(int, input().strip().split()))
for i in range(1, N+1):
    D.append(i)
for i in map(int, input().split()):
    mList.append(j)

def dial(num,p):
    right =0
    left =0
    while True:
        if D[p%len(D)] == num:
            left=len(D)-left
            del D[p%len(D)]
            break
        else:
            right+=1
            p+=1
    if right<left:
        if len(D) == 0: return 0, right
        return p,right
    else:
        if len(D) == 0: return 0, left
        return p, left

for i in mList:
    rPointer, rCount = dial(i,pointer)
    pointer = rPointer
    count +=rCount
print(count)