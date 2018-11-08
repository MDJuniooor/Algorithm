# https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3


def solution(s):
    answer = True
    num = ['1','2','3','4','5','6','7','8','9','0']
    for i in s:
        if not i in num:
            return False
    if len(s) == 4 or len(s) == 6:
        return True
    return False


print(solution("1234"))