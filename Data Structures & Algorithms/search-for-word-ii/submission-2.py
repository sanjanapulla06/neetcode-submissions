class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = {}

        # Build Trie
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["word"] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node:
                return

            node = node[ch]

            if "word" in node:
                result.append(node["word"])
                del node["word"]

            board[r][c] = "#"

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                        and board[nr][nc] != "#"):
                    dfs(nr, nc, node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result