T = int(input())
for case in range(T):
    show = list(map(int, input().strip().split()))
    data = list(map(int, input().strip().split()))
    queue =[i for i in range(show[0])]
    cnt = 0
    dic={}
    for i,v in enumerate(data):
        dic[str(i)]=v
    while True:
        maxNum = max(dic.values())
        if dic[str(queue[0])] == maxNum:
            cnt = cnt + 1
            if queue[0] == show[1]:
                print(cnt)
                break
            del dic[str(queue[0])]
            del queue[0]
        else:
            queue.append(queue.pop(0)) 

