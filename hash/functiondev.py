# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3


def solution(progresses, speeds):
    answer = []
    while True:
        print(progresses)
        cnt = 0
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt +=1
            if progresses == []:
                break
        if cnt is not 0:
            answer.append(cnt)
        if progresses == []:
            break
    print(answer)
    return answer

