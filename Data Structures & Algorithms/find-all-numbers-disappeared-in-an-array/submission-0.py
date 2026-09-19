class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for num in range(1, n + 1):
            if not num in nums:
                res.append(num)
        return res