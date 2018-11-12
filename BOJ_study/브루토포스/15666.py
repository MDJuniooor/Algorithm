import itertools
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in sorted(list(set(itertools.combinations_with_replacement(a, m)))):
    print(*i)
