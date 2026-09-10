from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        visits = []
        for i in range(len(username)):
            visits.append((timestamp[i], username[i], website[i]))
        visits.sort()
        users = defaultdict(list)
        for time, user, site in visits:
            users[user].append(site)
        pattern_count = defaultdict(int)
        for user in users:
            sites = users[user]
            patterns = set()
            for i in range(len(sites)):
                for j in range(i + 1, len(sites)):
                    for k in range(j + 1, len(sites)):
                        pattern = (sites[i], sites[j], sites[k])
                        patterns.add(pattern)
            for pattern in patterns:
                pattern_count[pattern] += 1
        answer = None
        best_score = 0
        for pattern, score in pattern_count.items():
            if score > best_score:
                best_score = score
                answer = pattern
            elif score == best_score and pattern < answer:
                answer = pattern
        return list(answer)