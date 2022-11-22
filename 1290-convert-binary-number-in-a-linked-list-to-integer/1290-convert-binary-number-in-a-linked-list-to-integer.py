# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n=head
        bnum=''
        while n!=None:
            bnum=bnum+str(n.val)
            n=n.next
        return int(bnum,2)
            
        