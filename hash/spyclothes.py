#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic = dict()
    answer = 1


    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]].append(clothes[i][0])
        else:
            dic[clothes[i][1]] = []
            dic[clothes[i][1]].append(clothes[i][0])

    for i in dic.keys():
        answer *= len(dic[i])+1
    return answer-1
