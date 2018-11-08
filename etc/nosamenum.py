# https: // programmers.co.kr/learn/courses/30/lessons/12906?language = python3


def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)):
        if arr[i] == answer[len(answer)-1]:
            continue
        answer.append(arr[i])
    # for i in arr:
    #     if answer[len(answer)-1] != i:
    #         answer.append(i) 
    # 이건 왜 안될까..?
    return answer
