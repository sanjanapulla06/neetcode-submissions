from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        queue = deque(students)
        i = 0
        unable = 0

        while queue:
            if queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                unable = 0
            else:
                queue.append(queue.popleft())
                unable += 1

                if unable == len(queue):
                    break

        return len(queue)