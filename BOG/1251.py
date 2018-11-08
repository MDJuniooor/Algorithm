data = input()
ans= []
for i in range(1,len(data)-1):
    for j in range(i+1,len(data)):
        temp = data[0:i][::-1]
        temp2 = data[i:j][::-1]
        temp3 = data[j:][::-1]
        ans.append(temp+temp2+temp3)
print(sorted(ans)[0])