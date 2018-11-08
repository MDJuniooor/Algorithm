# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
from collections import Counter, defaultdict
def solution(s):
    dic = defaultdict()
    counter = Counter(s.lower())
    dic['p'] = dic['y'] = 0
    for i in counter:
        dic[i] = counter[i]
    if dic['p'] == dic['y']:
        return True
    return False


print(solution('pPoooyY'))
