class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(r, c, size):
            val = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(val == 1, True)

            half = size // 2

            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)

            return Node(
                True, False,
                topLeft, topRight,
                bottomLeft, bottomRight
            )

        return dfs(0, 0, len(grid))