# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

def solution(s):
    strings = []
    for i in s:
        strings.append(i)
    return ''.join(sorted(strings, reverse=True))

print(solution("Zbcdefg"))
