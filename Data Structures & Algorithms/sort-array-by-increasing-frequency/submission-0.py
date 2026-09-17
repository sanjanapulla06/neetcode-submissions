class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        unique = list(freq.keys())

        unique.sort(key=lambda x: (freq[x], -x))

        ans = []

        for num in unique:
            ans.extend([num] * freq[num])

        return ans