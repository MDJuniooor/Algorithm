# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3
# ord chr to int
# chr int to chr
print(chr(ord('a')+1))


def solution(s, n):
    answer = []
    for i in s:
        code = ord(i)
        if code > 64 and code < 91:
            code = code + n
            while code > 90:
                code = code - 26
        elif code > 96 and code < 123:
            code = code + n
            while code > 122:
                code = code - 26
        answer.append(chr(code))
    return ''.join(answer)


print(solution("aY BC xXz",25))
