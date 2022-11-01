class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l=[]
        answer=""
        for i in sentence:
            if i not in l:
                l.append(i)
                answer=answer+i
        h=len(l)
        if h==26:
            return True
        else:
            return False
        