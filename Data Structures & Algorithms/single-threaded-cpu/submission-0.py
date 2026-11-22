import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = []

        for i, (start, duration) in enumerate(tasks):
            sorted_tasks.append((start, duration, i))

        sorted_tasks.sort()

        heap = []
        result = []

        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            if not heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < n and sorted_tasks[i][0] <= time:
                start, duration, index = sorted_tasks[i]
                heapq.heappush(heap, (duration, index))
                i += 1

            duration, index = heapq.heappop(heap)

            result.append(index)
            time += duration

        return result