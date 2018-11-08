# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

import functools

def solution(numbers):
    ns = list(map(str,numbers))
    ns.sort(key=functools.cmp_to_key(lambda x,y: int(x+y) - int(y+x)), reverse=True)
    answer = ''.join(ns)
    if int(answer) == 0:
        return '0'
    else :
        return ''.join(ns)


print(solution([0,0,0,0]))
