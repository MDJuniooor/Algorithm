# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
from time import time
def solution(number, k):
    cnt=0
    ans = [i for i in number]
    while cnt < k:
        check = True
        for i in range(len(ans)-1):
            if ans[i] < ans[i+1]:
                ans.pop(i)
                check = False
                break
        if check:
            ans.pop()
        cnt = cnt + 1
    return ''.join(ans)

start = time()
print(solution("1234567890"*100000,100))
print(time()-start)