class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        a=len(word1)
        b=len(word2)
        ans=""
        while i<a and j<b:
            ans=ans+word1[i]
            i=i+1
            ans=ans+word2[j]
            j=j+1
        if a<b:
            ans=ans+word2[a:]
        if a>b:
            ans=ans+word1[b:]
        return ans