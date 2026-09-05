class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            current_start = interval[0]
            current_end = interval[1]
            previous_end = result[-1][1]
            if current_start <= previous_end:
                result[-1][1] = max(previous_end, current_end)
            else:
                result.append(interval)
        return result
