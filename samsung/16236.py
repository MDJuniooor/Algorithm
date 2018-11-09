n = int(input())
sea = [[0]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]
meat =[]
baby = []
check = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(n):
    sea[i]= list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if sea[i][j] != 0 and sea[i][j] !=9:
            meat.append((i,j,sea[i][j]))
        if sea[i][j] == 9:
            baby = [i,j,2,0]
            visit[i][j]=True
def distance(current,meat,cnt,sea):
    