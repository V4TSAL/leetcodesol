class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        d=[]
        c=0
        for i in range(0,n+1):
            d.append(i)
        for n in d:
            c=0
            while n>0:
                n=n&(n-1)
                c=c+1
            ans.append(c)
        return ans