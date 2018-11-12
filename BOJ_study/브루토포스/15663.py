# import itertools
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# ans = set()
# for i in itertools.permutations(a, m):
#     ans.add(str(i).replace('(', '').replace(')', '').replace(',', ''))

# ans = sorted(list(ans))
# for i in ans:
#     print(i)

import sys
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
c = [False]*n
a = [0]*m
d = []


def go(index, n, m):
    if index == m:
        d.append(tuple(a))
        return
    for i in range(n):
        if c[i]:
            continue
        c[i] = True
        a[index] = num[i]
        go(index+1, n, m)
        c[i] = False


go(0, n, m)
d = sorted(list(set(d)))
for v in d:
    sys.stdout.write(' '.join(map(str, v))+'\n')

# import itertools
# import sys
# a, b = map(int, sys.stdin.readline().rstrip().split())
# li = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
# for i in sorted(list(set(itertools.permutations(li, b)))):
# 	print(*i)
