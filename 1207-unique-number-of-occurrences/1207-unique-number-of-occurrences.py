class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[] 
        v=[]
        for i in arr:
            if i not in v:
                vatsal=arr.count(i)
                l.append(vatsal)
                v.append(i)
        return len(l)==len(set(l))
        