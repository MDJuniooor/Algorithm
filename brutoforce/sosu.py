# https: // programmers.co.kr/learn/courses/30/lessons/42839?language = python3
import math
def getPrime(number):  # number가 소수이면 출력하는 함수
    if number == 1:
        return False
    if number == 2: 
        return True
    for x in range(2,round(math.sqrt(number)+1)):
        if number % x == 0:
            return False
    return True


def solution(numbers):
    numlist = []
    for i in numbers:
        numlist.append(i)
    for i in range(1,len(numbers)+1):
        testcase = []
        for j in range(i):
            
    return numlist

print(solution('17'))
