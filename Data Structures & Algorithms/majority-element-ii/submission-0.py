class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        n = len(nums)
        limit = n // 3

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if count > limit:
                result.append(num)

        return result