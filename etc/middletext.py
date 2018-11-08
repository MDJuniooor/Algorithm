# https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
import math
def solution(s):
    middle = math.ceil(len(s) / 2)
    if len(s) % 2 == 0:
        return s[middle-1:middle+1]
    else:
        return s[middle-1]


print(solution('c'))