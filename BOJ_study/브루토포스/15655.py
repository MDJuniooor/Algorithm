import itertools
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in itertools.combinations(a, m):
    print(str(i).replace('(', '').replace(')', '').replace(',', ''))
