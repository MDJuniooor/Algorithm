import sys

n = int(input())
xs = list(map(int, sys.stdin.readlines()))

stack = []
res = []
idx = 0

for i in range(1, n+1):
    stack.append(i)
    res.append('+')

    while stack and stack[-1] == xs[idx]:
        stack.pop()
        res.append('-')
        idx += 1

if stack:
    print('NO')
else:
    print('\n'.join(res))
