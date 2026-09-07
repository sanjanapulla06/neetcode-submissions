class Solution:
    def postorder(self, root):
        result = []
        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            result.append(root.val)
        dfs(root)
        return result