# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head 
        l=[]
        while a:
            if a not in l:
                l.append(a)
                a=a.next
            else:
                return a
        return None
            
        