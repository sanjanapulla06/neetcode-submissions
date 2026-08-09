class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            candidates = (num, curMax * num, curMin * num)
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(res, curMax)
        return res