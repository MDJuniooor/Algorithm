import itertools
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
for i in sorted(list(set(itertools.product(a,repeat=m)))):
    print(*i)