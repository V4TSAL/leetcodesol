class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        meow=max(candies)
        ans=[]
        for i in candies:
            if i+extraCandies>=meow:
                ans.append(True)
            else:
                ans.append(False)
        return ans