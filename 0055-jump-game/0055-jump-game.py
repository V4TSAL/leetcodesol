class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestPos = 0
        for curPos,jumpLength in enumerate(nums):
            if curPos <= farthestPos:
                farthestPos = max(farthestPos, curPos+jumpLength)
            else:
                return False
            if farthestPos>=len(nums)-1:
                return True