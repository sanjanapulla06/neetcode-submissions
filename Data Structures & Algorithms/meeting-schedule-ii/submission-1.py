import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        room_ends = []
        for interval in intervals:
            current_start = interval.start
            current_end = interval.end
            if room_ends and room_ends[0] <= current_start:
                heapq.heappop(room_ends)
            heapq.heappush(room_ends, current_end)
        return len(room_ends)