data = input()
ans = [0 for i in range(97,123)]
for i in data:
    ans[ord(i)-97] = ans[ord(i)-97] + 1

for i in ans:
    print('{}'.format(i),end=' ')
