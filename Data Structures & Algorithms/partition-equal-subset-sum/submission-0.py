class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        possible_sums = {0}
        for n in nums:
            new_sums = set()
            for s in possible_sums:
                new_sums.add(s)
                new_sums.add(s + n)
            possible_sums = new_sums
        return target in possible_sums