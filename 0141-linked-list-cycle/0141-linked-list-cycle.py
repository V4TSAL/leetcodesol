class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
	    slow = fast = head #slow and fast pointers
	    while fast and fast.next: #while not at the end of the list
		    slow = slow.next #slow moves forward by 1
		    fast = fast.next.next #fast moves forward by 2
		    if slow == fast: #if they are the same then we must have a cycle!
			    return True
	    return False #no cycle found