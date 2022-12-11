class Solution:
    def maxPathSum(self, root, s = -inf) -> int:
        def dfs(n):                     
            nonlocal s                 
            if not n : return 0        
            l = max(0, dfs(n.left))    
            r = max(0, dfs(n.right))   
            s = max(s, l + r + n.val)  
            return n.val + max(l, r)   
        dfs(root)
        return s