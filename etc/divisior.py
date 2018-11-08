# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        return [-1]
    answer.sort()
    return answer


print(solution([2, 36, 1, 3], 1))
