import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(heap, (-time, tweetId, user, index))

        result = []

        while heap and len(result) < 10:
            time, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            if index > 0:
                prev_time, prev_tweetId = self.tweets[user][index - 1]

                heapq.heappush(
                    heap,
                    (-prev_time, prev_tweetId, user, index - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)