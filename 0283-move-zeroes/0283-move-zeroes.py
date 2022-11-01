class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        c=0
        while i<=len(nums)-1:
            if nums[c]==0:
                nums.remove(0)
                nums.append(0)
                i=i+1
            else:
                i=i+1
                c=c+1
        return nums