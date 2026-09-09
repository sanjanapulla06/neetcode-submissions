class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        white_count = 0
        minimum = float('inf')
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                white_count += 1
            if right - left + 1 == k:
                minimum = min(minimum, white_count)
                if blocks[left] == 'W':
                    white_count -= 1
                left += 1
        return minimum