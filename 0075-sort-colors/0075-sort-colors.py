class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        zero=0
        one=0
        two=0
        for i in nums:
            if i==0:
                zero=zero+1
            if i==1:
                one=one+1
            if i==2:
                two=two+1
        nums[0:zero]=[0]*zero
        nums[zero:zero+one]=[1]*one
        nums[one+zero:zero+two+one]=[2]*two