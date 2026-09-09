class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build the graph
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):

            # We found a node we've already visited → cycle
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:

                # Ignore the node we came from
                if neighbor == parent:
                    continue

                # If DFS finds a cycle
                if not dfs(neighbor, node):
                    return False

            return True

        dfs(0, -1)

        # Every node must have been visited
        return len(visited) == n