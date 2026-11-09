from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dest in tickets:
            graph[src].append(dest)

        for src in graph:
            graph[src].sort(reverse=True)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]