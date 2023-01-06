class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        for i in costs:
            if coins-i>=0:
                ans=ans+1
                coins=coins-i
            else:
                break
        return ans
                