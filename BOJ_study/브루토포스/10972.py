n = int(input())
L = list(map(int, input().split()))

i = n-1
while i > 0 and L[i] <= L[i-1]:
    i -= 1
if i <= 0:
    print(-1)
else:
    j = n-1
    while L[j] <= L[i-1]:
        j -= 1
    L[i-1], L[j] = L[j], L[i-1]
    j = n-1
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
    for i in L:
        print(i, end=' ')
    print()
