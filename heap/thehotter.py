# https://programmers.co.kr/learn/courses/30/lessons/42626


def solution(scoville, K):
    from heapq import heappush, heappop
    cnt = 0
    hq = []
    for i in scoville:
        heappush(hq, i)
    
    while 1:
        if len(hq) < 2:
            if hq[0] < K:
                return -1
            else:
                break
        heappush(hq, heappop(hq)+heappop(hq)*2)
        cnt += 1
        
        if hq[0] >= K:
            break
    return cnt


print(solution([11,22,33,44,1, 2, 3, 9, 10, 12],7))
