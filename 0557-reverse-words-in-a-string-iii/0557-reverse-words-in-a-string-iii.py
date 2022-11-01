class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(" ")
        lst=[]
        answer=""
        for i in a:
            lst.append(i[::-1])
        i=0
        for j in lst:
            if i!=len(lst)-1:
                answer=answer+j+" "
                i=i+1
            else:
                answer=answer+j
        return answer
        
        