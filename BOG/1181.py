n = int(input())
voca = set()
for i in range(n):
    voca.add(input())
voca = list(voca)

voca.sort(key=lambda x: (len(x),x))
for i in voca:
    print(i)
