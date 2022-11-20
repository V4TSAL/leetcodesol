# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[root]
        nq=[]
        l=[]
        result=[]  
        if root is None:
            return []
        while len(q)!=0:
            for root in q:
                l.append(root.val)
                if root.left is not None:
                    nq.append(root.left)
                if root.right is not None:
                    nq.append(root.right)
            result.append(l)
            l=[]
            q=nq
            nq=[]
        return result