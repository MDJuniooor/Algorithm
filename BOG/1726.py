# 1 = 동, 2 = 서, 3 = 남, 4 = 북
m,n = map(int, input().split())
factory = [[] for _ in range(m)]
goal = []
for i in range(m):
    factory[i] = list(map(int, input().split()))
for _ in range(2):
    x,y,z = map(int, input().split())
    goal.append((x-1,y-1,z))
print(goal)