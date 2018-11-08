L,C = map(int, input().split())
voca = list(input().split())
voca.sort()
ary = set()
moum = ['a','e','i','o','u']

def process(idx, string):
    if len(string) == L:        
        check = False
        cnt = 0
        for m in moum:
            if m in string:
                check=True
                cnt+=1
        if check and len(string)-cnt > 1:
            ary.add(string)
    if idx >= C:
        return
                
    process(idx+1,string)
    process(idx+1,string+voca[idx])

process(0,'')
for i in sorted(list(ary)):
    print(i)
