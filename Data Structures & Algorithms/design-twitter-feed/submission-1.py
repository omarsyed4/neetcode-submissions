        
class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.time = 0
        self.heap = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.heap, (-self.time, userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        temp = []

        while self.heap and len(res) < 10:
            # pop from heap
            t, tweetUserId, tweetId = heapq.heappop(self.heap)

            # make sure the id is in the following or if its their own
            if tweetUserId == userId:
                res.append(tweetId)

            elif tweetUserId in self.users[userId]:
                res.append(tweetId)

            # add it to the temp
            temp.append((t, tweetUserId, tweetId))

        
        # push all temp back into the heap
        for tup in temp:
            t, tweetUserId, tweetId = tup
            heapq.heappush(self.heap, (t, tweetUserId, tweetId))

        return res
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        


