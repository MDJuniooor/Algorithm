import itertools
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
li = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
for i in sorted(list(set(itertools.combinations(li, b)))):
	print(*i)
