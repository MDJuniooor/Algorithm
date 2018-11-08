# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
    m1 = [1, 2, 3, 4, 5] * 2000
    m2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == m1[i]:
            cnt[0] = cnt[0] + 1
        if answers[i] == m2[i]:
            cnt[1] = cnt[1] + 1
        if answers[i] == m3[i]:
            cnt[2] = cnt[2] + 1
    sol = []
    for i in range(3):
        if max(cnt) > cnt[i]:
            cnt[i] = 0
    for i in range(3):
        if cnt[i] != 0:
            sol.append(i+1)
    return sol


print(solution([1, 2, 3, 4, 5]))
