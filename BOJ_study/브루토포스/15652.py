import sys
n, m = map(int, input().split())
a = [0]*m


def go(idx, MIN):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(MIN, n+1):
        a[idx] = i
        go(idx+1,i)


go(0,1)

# import itertools
# n, m = map(int, input().split())
# [print(' '.join(x))for x in list(
#     itertools.combinations_with_replacement([str(i+1) for i in range(n)], m))]
