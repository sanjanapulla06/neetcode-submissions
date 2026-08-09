class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            
            self.diameter = max(self.diameter, leftDepth + rightDepth)
            
            return 1 + max(leftDepth, rightDepth)
        
        depth(root)
        return self.diameter