import heapq

class Solution:
    def pickGifts(self, gifts, k):
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            largest = int(largest ** 0.5)
            heapq.heappush(heap, -largest)

        return -sum(heap)