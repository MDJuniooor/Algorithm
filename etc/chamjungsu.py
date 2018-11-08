def findsosu(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return s

class Solution:
    def solution(self, a, b):
        cnt = 0
        ary = findsosu(b+11)
        for i in range(a,b+1):
            check = False
            for j in range(i-10,i+11):
                if ary[j] == 1:
                    check = True
            if not check:
                cnt+=1
        print(cnt)
        return 0
