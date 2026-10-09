class Solution:
    def mySqrt(self, x: int) -> int:
        y = 0

        while (y + 1) * (y + 1) <= x:
            y += 1

        return y