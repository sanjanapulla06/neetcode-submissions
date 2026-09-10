class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, current):
            if not root:
                return 0

            current = current * 10 + root.val

            if root.left is None and root.right is None:
                return current

            return dfs(root.left, current) + dfs(root.right, current)

        return dfs(root, 0)