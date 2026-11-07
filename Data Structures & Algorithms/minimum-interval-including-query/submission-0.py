import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        sorted_queries = sorted(queries)

        heap = []
        result = {}

        i = 0

        for q in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Smallest valid interval
            if heap:
                result[q] = heap[0][0]
            else:
                result[q] = -1

        return [result[q] for q in queries]