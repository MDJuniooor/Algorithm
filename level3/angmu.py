# https://programmers.co.kr/learn/courses/30/lessons/43104?language=python3


def solution(N):
    ans = [0 for i in range(N+2)]
    ans[1] = 1
    for i in range(2,N+2):
        ans[i] = ans[i-1] + ans[i-2]
    return (ans[N+1]+ans[N])*2 
print(solution(5))