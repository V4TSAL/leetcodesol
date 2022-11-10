class Solution:
    def removeDuplicates(self, s: str) -> str:
        v=[]
        answer=""
        for i in s:
            l=len(v)
            if l==0:
                v.append(i)
            else:
                if v[l-1]==i:
                    v.pop()
                else:
                    v.append(i)
        # v=v[::-1]
        for i in v:
            answer=answer+i
        return answer