import itertools
import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in itertools.product(a, repeat=m):
    sys.stdout.write(str(i).replace('(', '').replace(')', '').replace(',', ''))
