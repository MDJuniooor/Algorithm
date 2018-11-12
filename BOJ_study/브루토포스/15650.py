import itertools
n,m=map(int,input().split())
p=[i for i in range(1,n+1)]
for i in itertools.combinations(p,m):
    print(str(i).replace('(', '').replace(')', '').replace(',', ''))
