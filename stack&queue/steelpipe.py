# https://programmers.co.kr/learn/courses/30/lessons/42585

def solution(arrangement):
    st = []
    answer = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            st.append(i)
        else:
            st.pop()
            if arrangement[i-1] == '(':
                answer += len(st)
            else:
                answer +=1
    return answer

