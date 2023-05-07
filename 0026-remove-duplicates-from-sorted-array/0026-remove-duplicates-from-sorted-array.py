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
                
        /*hello vatsal, you can also create two pointers as i, j
        initializing  to 1
        Now can you can run a loop starting from 1 position and check whether the current element is equal to previos element , if it is then you can increase you value of j until this condition breaks and then you can 
        place that jth index element in i-th position by this way your remova will be done in 1 iteration and inplace also.
        If you like my contribution i would be we very happy
        
        */
            
            
            
