class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[]
        for i in strs:
            l.append(len(i))
        x=min(l)
        ans=""
        for i in range(x):
            temp=strs[0][i]
            for j in strs:
                if j[i]==temp:
                    pass
                else:
                    return ans
            ans=ans+temp
        return ans
        
        
                    
            