dwarf =[]
ans = []
sol = []
for _ in range(9):
    dwarf.append(int(input()))
total = sum(dwarf)
for i in range(9):
    for j in range(i+1,9):
        if total - dwarf[i] - dwarf[j] == 100:
            ans.append([i,j])
            break        

for i in range(9):
    if i not in ans[0]:
        sol.append(dwarf[i])

for i in sorted(sol):
    print(i)