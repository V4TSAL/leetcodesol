class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=nums[0]
        k=1
        for i in nums:
            for j in nums[k:]:
                if i==j:
                    nums.remove(i)
            k=k+1
        return len(nums)
                
            
            
            