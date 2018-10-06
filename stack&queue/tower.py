# https://programmers.co.kr/learn/courses/30/lessons/42588


def solution(heights):
    answer = [0 for x in range(len(heights))]
    for i in range(1,len(heights)):
        for j in range(i,-1,-1):
            print(i,j)
            if heights[j] > heights[i]:
                answer[i]=j+1
                break
    return answer


solution([1, 5, 3, 6, 7, 6, 5])
