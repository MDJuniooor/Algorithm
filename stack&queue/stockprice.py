#https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3


def solution(prices):
    answer = [0 for x in range(len(prices))]

    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer

