# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        n=head
        prev=None
        while n!=None:
            if n.val==val and prev==None:
                head=n.next
                prev=None
                n=n.next
            elif n.val==val:
                prev.next=n.next
                n=n.next
            else:
                prev=n
                n=n.next
        return head
        
        
        