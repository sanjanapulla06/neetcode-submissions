class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        for num in range(1, n + 1):
            if num not in seen:
                missing = num
                break

        return [duplicate, missing]