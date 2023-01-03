class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l1=len(strs)
        c=0
        l2=len(strs[0])
        for i in range(l2):
            for j in range(1,l1):
                if strs[j-1][i]>strs[j][i]:
                    c=c+1
                    break
        return c    