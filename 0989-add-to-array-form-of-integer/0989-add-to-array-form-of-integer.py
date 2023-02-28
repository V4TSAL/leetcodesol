class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a=''
        for i in num:
            a=a+str(i)
        b=int(a)+k
        b=str(b)
        ans=[]
        for i in b:
            ans.append(int(i))
        return ans