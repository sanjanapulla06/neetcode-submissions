class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num - 1 not in num_set:
                a=num
                curr=1
                while a + 1 in num_set:
                    a += 1
                    curr += 1
                longest = max(longest, curr)
        return longest
