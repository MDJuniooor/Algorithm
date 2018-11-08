# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    citations.sort(reverse=True)
    answer=0
    for i in range(0,len(citations)):
        
        if citations[i] > i:
            answer+=1
        else:
            return answer
    return answer
