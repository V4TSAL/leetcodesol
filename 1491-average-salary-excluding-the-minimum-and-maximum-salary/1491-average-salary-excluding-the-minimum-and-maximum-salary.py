class Solution:
    def average(self, salary: List[int]) -> float:
        a=max(salary)
        b=min(salary)
        c=sum(salary)
        return (c-(a+b))/(len(salary)-2)