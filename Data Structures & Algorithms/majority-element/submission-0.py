class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        limit = n // 2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > limit:
                return num