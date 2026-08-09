class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)   #dp[i] stores the no.of set bits in i
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)  #right shift i by 1 and check last bit using i&1
        return dp