class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        seen = set()
        repeated = -1
        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                else:
                    seen.add(num)
        missing = -1
        for num in range(1, n * n + 1):
            if num not in seen:
                missing = num
                break
        return [repeated, missing]