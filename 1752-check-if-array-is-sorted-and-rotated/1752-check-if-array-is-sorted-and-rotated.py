class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        temp=nums[0]
        l=len(nums)
        for i in range(l-1):
            if nums[i]<=nums[i+1]:
                c=c+1
            else:
                break
        meow=l-1-c
        if c==l-1:
            return True
        for i in range(meow):
            a=nums[-1]
            nums.pop()
            nums.insert(0,a)
        sha=0
        for i in range(l-1):
            if nums[i]<=nums[i+1]:
                sha=sha+1
            else:
                break
        if sha==l-1:
            return True
        else:
            return False
        
        
#         
            
            
        