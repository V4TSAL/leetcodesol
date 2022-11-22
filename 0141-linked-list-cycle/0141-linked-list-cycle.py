# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=[]
        n=head
        while n!=None:
            if n not in l:
                l.append(n)
                n=n.next
            else:
                return True
                break
        return False
            