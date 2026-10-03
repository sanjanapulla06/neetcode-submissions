class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}

        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        res = []

        for num in arr2:
            for _ in range(freq[num]):
                res.append(num)
            del freq[num]

        remaining = []

        for num in freq:
            for _ in range(freq[num]):
                remaining.append(num)

        remaining.sort()

        res.extend(remaining)

        return res