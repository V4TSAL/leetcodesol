# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        if head is None:
            return head
        else:
            n=head
            prev=None
            nxt=n.next
            while n!=None:
                nxt=n.next
                n.next=prev
                prev=n
                n=nxt
            head=prev
            return head
            
            
            
        