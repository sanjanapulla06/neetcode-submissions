class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)

        if root is None:
            return newNode

        curr = root

        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = newNode
                    break
                curr = curr.left

            else:
                if curr.right is None:
                    curr.right = newNode
                    break
                curr = curr.right

        return root