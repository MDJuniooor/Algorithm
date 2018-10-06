# 10진법을 3진법 변환 + 3을 4로 치환


def trans(n):
    answer = []
    while n>0:
        answer.append(n%3)
        n//=3
    return answer

def solution(n):  
    sol = ''
    answer = trans(n)
    answer.reverse()
    while 1:
        zero = False
        for j in range(len(answer)):
            if j==0:
                continue
            if answer[j] == 0:
                answer[j] = 4
                if answer[j-1]==1:
                    answer[j-1] = 0
                    zero = True
                elif answer[j-1] == 2:
                    answer[j-1] = 1
                elif answer[j-1] == 4:
                    answer[j-1] = 2
        if not zero:
            break
    for i in answer:
        sol=sol+str(i)
    return int(sol)
