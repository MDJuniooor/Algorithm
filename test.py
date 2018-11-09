class Solution:
    def find(self, left, right):
        cnt = 0
        for i in range(left, right+1):
            string = str(i)
            for j in range(1,len(string)):
                if string[j-1] == '3' and string[j] == '6':
                    print(string)
                    cnt+=1
                    break
        return cnt

S = Solution()
print(S.find(3600,3636))