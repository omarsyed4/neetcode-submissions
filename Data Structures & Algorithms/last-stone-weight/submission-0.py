class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            # Get the two heaviest stones. 
            X = heapq.heappop(heap)
            Y = heapq.heappop(heap)

            # make both pos
            X = -X
            Y = -Y

            # If x is less than y, get rid of x. 
            # Subtract x from y. 
            if X != Y:
                new = X - Y
                heapq.heappush(heap, -new)
        
        if heap:
            return -heap[0]
        else:
            return 0

