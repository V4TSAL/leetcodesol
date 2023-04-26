class Solution:
    def addDigits(self, num: int) -> int:
        a=str(num)
        if len(a)==1:
            return num
        print(len(a))
        while len(a)>1:
            temp=0
            for i in a:
                temp=temp+int(i)
            a=str(temp)
        return int(a)
        
        
        