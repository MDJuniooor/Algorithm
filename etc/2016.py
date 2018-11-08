# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3




def solution(a, b):
    answer = ''
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    cnt = 0
    for i in range(a-1):
        cnt = cnt + month[i]
    cnt = cnt + b
    return day[cnt % 7]


print(solution(1,2))
