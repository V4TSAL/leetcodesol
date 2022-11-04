class Solution:
    def reverseVowels(self, s: str) -> str:
        v=""
        c=0
        l=['a','e','i','o','u']
        a=[]
        ans=""
        for i in s:
            a.append(i)
            if i.lower() in l:
                v=v+i
        v=v[::-1]
        for j in range(len(s)):
            if a[j].lower() in l:
                a[j]=v[c]
                c=c+1

        for k in a:
            ans=ans+k
        return ans        
        