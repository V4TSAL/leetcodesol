class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        d=c+1
        temp=0
        while c<len(nums)-1:
            if nums[c]==0:
                while d<len(nums):
                    if nums[d]!=0:
                        nums[c]=temp
                        nums[c]=nums[d]
                        nums[d]=temp
                        break
                    else:
                        d=d+1
                c=c+1
                d=c+1
            else:
                c=c+1
                d=c+1
            
                        