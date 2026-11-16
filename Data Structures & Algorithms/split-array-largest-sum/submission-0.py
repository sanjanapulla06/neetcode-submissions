class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            subarrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num <= mid:
                    curr_sum += num
                else:
                    subarrays += 1
                    curr_sum = num

            if subarrays <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left