class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        previous_end = intervals[0][1]
        for interval in intervals[1:]:
            current_start = interval[0]
            if current_start < previous_end:
                count += 1
            else:
                previous_end = interval[1]
        return count