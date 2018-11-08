# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
def solution(strings, n):
    for i in range(1, len(strings)):
        for j in range(0, len(strings)-1):
            if strings[i][n] < strings[j][n]:
                strings[i], strings[j] = strings[j], strings[i]
            elif strings[i][n] == strings[j][n] and strings[i] < strings[j]:
                strings[i], strings[j] = strings[j], strings[i]
    return strings
print(solution(["abce", "abcd", "cdx"],2))
