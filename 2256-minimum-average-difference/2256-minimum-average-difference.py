class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        v=sum(nums)
        l=[]
        s=0
        s1=0
        meow=0
        for i in range(len(nums)):
            s1=s1+nums[i]
            s=(s1)//(i+1)
            if len(nums)-(i+1)!=0: 
                meow=(v-s1)//(len(nums)-(i+1))
                l.append(abs(s-meow))
            else:
                l.append(s)
        print(l)
        return l.index(min(l))
            
            