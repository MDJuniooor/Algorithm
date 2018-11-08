from collections import deque
M,N = map(int, input().split())
box = [[0]*M for i in range(N)] # M*N
visit = [[0]*M for i in range(N)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
for i in range(len(box)):
    box[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i,j])

while queue:
    current = []
    check = False
    for _ in range(len(queue)):
        y, x = queue.popleft()
        visit[y][x]=1
        current.append([y,x])
    for y, x in current:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            else:
                if box[ny][nx] == 0 and visit[ny][nx] == 0:
                    check = True
                    box[ny][nx] = 1
                    visit[ny][nx] = 1
                    queue.append([ny, nx])
                if box[ny][nx] == 1 and visit[ny][nx] == 0:
                    box[ny][nx] = 1
                    visit[ny][nx] = 1
                    queue.append([ny, nx])
    if not check:
        break
    cnt+=1


check = False
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            check = True

if check:
    print(-1)
else:
    print(cnt)
