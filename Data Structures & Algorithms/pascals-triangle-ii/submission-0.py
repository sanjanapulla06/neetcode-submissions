class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex + 1):
            curr = [1] * (i + 1)
            if i > 0:
                prev = res[i - 1]
                for j in range(1, len(curr) - 1):
                    curr[j] = prev[j - 1] + prev[j]
            res.append(curr)
        return res[rowIndex]