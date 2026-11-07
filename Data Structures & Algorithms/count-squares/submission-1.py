from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (x1, y1), freq in self.points.items():

            if abs(x1 - x) == abs(y1 - y) and x1 != x and y1 != y:

                total += (
                    freq
                    * self.points.get((x1, y), 0)
                    * self.points.get((x, y1), 0)
                )

        return total