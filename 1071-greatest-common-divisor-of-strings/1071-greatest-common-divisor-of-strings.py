class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        meow=""
        w=min(len(str1),len(str2))
        last_successful = ""
        for i in range(w):
            if str1[i]==str2[i]:
                meow=meow+str1[i]
            elif str1[i]!=str2[i]:
                return ""
            if meow*int(len(str1)/len(meow))==str1 and \
                meow*int(len(str2)/len(meow))==str2:
                last_successful = meow
        return last_successful
                