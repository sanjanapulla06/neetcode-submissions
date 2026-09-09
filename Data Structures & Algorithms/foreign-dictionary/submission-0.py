class Solution:
    def foreignDictionary(self, words):

        graph = {}

        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = []

        indegree = {}

        for char in graph:
            indegree[char] = 0

        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            found_difference = False

            for j in range(min(len(word1), len(word2))):

                if word1[j] != word2[j]:

                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1

                    found_difference = True
                    break

            if not found_difference and len(word1) > len(word2):
                return ""

        queue = []

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:

            char = queue.pop(0)
            result.append(char)

            for neighbor in graph[char]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(graph):
            return ""

        return ''.join(result)