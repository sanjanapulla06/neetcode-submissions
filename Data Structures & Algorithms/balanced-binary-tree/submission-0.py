class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        
        def depth(node):
            if not node:
                return 0
            
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            
            if abs(leftDepth - rightDepth) > 1:
                self.balanced = False
            
            return 1 + max(leftDepth, rightDepth)
        
        depth(root)
        return self.balanced