# https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
def solution(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return sum(s)
print(solution(10))


# def solution(n):
#     num = set(range(2, n+1))

#     for i in range(2, n+1):
#         if i in num:
#             num -= set(range(2*i, n+1, i))
#     return len(num)
