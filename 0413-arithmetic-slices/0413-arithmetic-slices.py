class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l=len(nums)
        x=0
        if l<3:
            return 0
        c=0
        result=0
        temp=nums[1]-nums[0]
        for i in range(1,l-1):
            if temp==nums[i+1]-nums[i]:
                c=1+c
                print("First ",temp,nums[i+1]-nums[i])
                result=result+c
            else:
                c=0
                temp=nums[i+1]-nums[i]
                x=x+1
        return result
    
    