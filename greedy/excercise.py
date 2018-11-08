# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3


def solution(n, lost, reserve):
    answer = [1 for x in range(n+1)]
    for i in reserve:
        answer[i] = 2
    for i in lost:
        answer[i] = answer[i]-1
    for i in range(1,len(answer)-1):
        if answer[i] == 0 and answer[i+1] == 2:
            answer[i]=answer[i+1]=1
            continue
        if answer[i] == 0 and answer[i-1] == 2:
            answer[i]=answer[i-1]=1
            continue
    if answer[n-1] ==2 and answer[n] ==0:
        answer[n-1]=answer[n]=1
    cnt = 0
    for i in range(1,len(answer)):
        if answer[i] !=0:
            cnt=cnt+1
    return cnt


print(solution(n=5 , lost=[2, 3, 4] ,reserve=[3, 4, 5]))
