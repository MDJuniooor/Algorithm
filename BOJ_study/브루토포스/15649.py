import sys
n, m = map(int, input().split())
c = [False]*(n+1)
a = [0]*m

def go(idx):
    if idx == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[idx] = i
        go(idx+1)
        c[i] = False

go(0)

# import itertools
# N, M = map(int, input().split())
# p = [i for i in range(1, N + 1)]
# for i in itertools.permutations(p, M):
#     print(str(i).replace('(', '').replace(')', '').replace(',', ''))
