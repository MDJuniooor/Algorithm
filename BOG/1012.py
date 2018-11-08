import sys
sys.setrecursionlimit(100000)
def DFS(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[x][y] = 1

    for a in range(4):
        tx = x + dx[a]
        ty = y + dy[a]

        if (tx >= 0 and ty >= 0 and tx < M and ty < N):
            if (grid[tx][ty] == 1 and visited[tx][ty] == 0):
                DFS(tx, ty)


for _ in range(int(input())):
    M, N, cab = map(int, sys.stdin.readline().split())
    grid = [[0]*N for i in range(M)]
    visited = [[0]*N for i in range(M)]
    bug = 0
    for __ in range(cab):
        a, b = map(int, sys.stdin.readline().split())
        grid[a][b] = 1

    for i in range(M):
        for j in range(N):
            if (grid[i][j] == 1 and visited[i][j] == 0):
                DFS(i, j)
                bug += 1
    print(bug)
