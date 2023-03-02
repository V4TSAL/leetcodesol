class Solution:
    def compress(self, chars: List[str]) -> int:
        c=0
        i=0
        l=len(chars)
        meow1=[]
        meow2=[]
        vat=[]
        while c<l:
            a=chars[c]
            j=0
            for i in range(c,l):
                if a==chars[i]:
                    j=j+1
                    c=c+1
                else:
                    break
            vat.append(a)
            vat.append(str(j))
            meow2.append(vat)
            vat=[]
        print(meow2)
        # for i in range(l):
        #     c=0
        #     # if chars[i] not in meow1:
        #     meow1.append(chars[i])
        #     for j in range(i,l):
        #         if chars[i]==chars[j]:
        #             c=c+1
        #         else:
        #             break
        #     vat.append(chars[i])
        #     vat.append(str(c))
        #     meow2.append(vat)
        #     vat=[]
        # print(meow2)
        
        # for i in range(len(set(chars))*2):
        #     chars[i]=meow2[i][0]
        #     c=0
        #     for j in range(i+1,len(meow2[i][1])+i):
        #         sh=meow2[i][0]
        #         chars[j]=sh[c]
        #         c=c+1
        # print(chars)
        # *********************************
        xyz=0
        dd=0
        kk=0
        if len(chars)==1:
            return len(chars)
        while dd<=len(meow2)-1:
            chars[xyz]=meow2[dd][0]
            xyz=xyz+1
            c=0
            for j in range(xyz,len(meow2[dd][1])+xyz):
                if meow2[dd][1]!='1':
                    chars[j]=meow2[dd][1][c]
                    c=c+1
                    xyz=xyz+1
            dd=dd+1
        chars=chars[:xyz]
        return len(chars)
            
            
        