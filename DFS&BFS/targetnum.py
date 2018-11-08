# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3


def solution(numbers, target):
    idx = 0
    ans = []
    while numbers:
        x = numbers.pop()
        ans.append([x,idx])
        ans.append([-x,idx])

print(solution([1, 1, 1, 1, 1],	3))
