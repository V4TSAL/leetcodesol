class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        for i in nums:
            p=p*i
        if p>0:
            return 1
        if p<0:
            return -1
        if p==0:
            return 0