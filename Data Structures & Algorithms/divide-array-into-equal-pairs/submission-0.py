class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num] % 2 != 0:
                return False
        return True