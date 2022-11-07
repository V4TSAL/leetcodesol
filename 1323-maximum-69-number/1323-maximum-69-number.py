class Solution:
    def maximum69Number (self, num: int) -> int:
        a=str(num)
        l=[]
        for i in a:
            l.append(int(i))
        for i in range(len(a)):
            if l[i]==6:
                l[i]=9
                break
        ans=""
        for i in l:
            ans=ans+str(i)
        return int(ans)
        
        