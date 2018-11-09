queue =[]
pointer=0
count=[]
N, M = map(int, input().split())
L = list(map(int, input().strip().split()))
for i in range(1, N+1):
    queue.append(i)
pointer = M

def solution(queue,pos,next,cnt):
    tmp = queue[:]
    # print(tmp)
    if next == len(L):
        count.append(cnt)
        return
    left = len(tmp) - 1
    right = pos + 1
    nextpos = 0
    for i in range(len(tmp)):
        if L[next] == tmp[i]:
            nextpos = i
            break
    if abs(pos-nextpos) == 0:
        del tmp[0]
        solution(tmp,pos,next+1,cnt)
    else:
        tmp = tmp[nextpos:]+tmp[:nextpos] 
        test = [abs(left-nextpos), abs(right-nextpos)]
        solution(tmp, 0, next, cnt+min(test)+1)


solution(queue,0,0,0)
print(count[0])
