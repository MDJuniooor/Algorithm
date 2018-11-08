from collections import deque
n, m, v = map(int, input().split())
ary = [[0]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    ary[x][y] = ary[y][x] = 1

def dfs(num):
    print(num,end=" ")
    for i in range(1, n+1):
        if ary[num][i] and visit[i] == 0:
            visit[i] = 1
            dfs(i)

def bfs(start):
    queue = deque()
    for i in range(1,n+1):
        visit[i]=0
    queue.append(start)
    visit[start] = 1

    while queue:
        num = queue.popleft()
        print(num,end=" ")

        for i in range(1,n+1):
            if ary[num][i] and visit[i] == 0:
                visit[i] = 1
                queue.append(i)
    print()


visit[v] = 1
dfs(v)
print()
bfs(v)
