class Solution:
    def makeGood(self, s: str) -> str:
        l=len(s)
        v=[]
        answer=""
        for i in s:
            v.append(i)
        c=0
        while c<l-1:
            if ((v[c].islower() and v[c+1].isupper()) or(v[c].isupper() and v[c+1].islower()))  and ((v[c]==v[c+1].lower()) or (v[c].lower()==v[c+1])):
                v.pop(c)
                v.pop(c)
                l=len(v)
                c=0
            else:
                c=c+1
        for i in v:
            answer=answer+i
        return answer
        
        