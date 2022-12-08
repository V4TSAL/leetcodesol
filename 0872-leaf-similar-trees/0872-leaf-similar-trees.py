class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeaf(node,leaf):
            if node:
                if not node.left and not node.right:
                    leaf.append(node.val)
                getLeaf(node.left,leaf)
                getLeaf(node.right,leaf)
            return leaf
        
        return getLeaf(root1,[])==getLeaf(root2,[])