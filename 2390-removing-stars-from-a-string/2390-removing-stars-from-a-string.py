class Solution:
    def removeStars(self, s: str) -> str:
        l=len(s)
        v=[]
        answer=""
        for i in s:
            if len(v)==0:
                v.append(i)
            else:
                if i=='*':
                    v.pop()
                else:
                    v.append(i)
        for i in v:
            answer=answer+i
        return answer