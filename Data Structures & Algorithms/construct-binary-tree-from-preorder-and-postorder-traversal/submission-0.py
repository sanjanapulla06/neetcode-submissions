class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {val: i for i, val in enumerate(postorder)}

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])

            if pre_start == pre_end:
                return root

            left_root = preorder[pre_start + 1]

            left_size = pos[left_root] - post_start + 1

            root.left = build(
                pre_start + 1,
                pre_start + left_size,
                post_start,
                post_start + left_size - 1
            )

            root.right = build(
                pre_start + left_size + 1,
                pre_end,
                post_start + left_size,
                post_end - 1
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)