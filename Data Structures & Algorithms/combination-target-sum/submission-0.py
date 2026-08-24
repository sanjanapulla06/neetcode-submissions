from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, remaining - nums[i])
                current.pop()
        backtrack(0, target)
        return result