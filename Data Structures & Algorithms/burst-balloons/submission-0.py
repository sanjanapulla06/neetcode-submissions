class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = {}
        for l in range(n-1, -1, -1):
            for r in range(l+1, n):
                maxCoins = 0
                for k in range(l+1, r):
                    coins = nums[l] * nums[k] * nums[r]
                    coins += dp.get((l, k), 0) + (dp.get((k, r), 0))
                    maxCoins = max(maxCoins, coins)
                    dp[(l, r)] = maxCoins
        return dp.get((0, n - 1), 0)
