# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left)+[root.val]+ self.inorderTraversal(root.right)
            # l.append()
            # l.append()
        # print(l)
        # return (l)
        # for i in l:
        #     if i.isdigit():
        #         answer.append(i)
        # return answer
        
            
    # def helper( self , )