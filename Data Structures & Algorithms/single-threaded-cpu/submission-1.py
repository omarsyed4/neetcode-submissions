class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = [(start, duration, i) for i, (start, duration) in enumerate(tasks)]
        tasks.sort()

        time = 0

        res = []

        heap = []
        ptr = 0
        
        while ptr < len(tasks) or heap:

            if not heap and ptr < len(tasks):
                time = max(time, tasks[ptr][0])

            # find all tasks avail
            while ptr < len(tasks) and tasks[ptr][0] <= time:
                (start, duration, i) = tasks[ptr]
                heapq.heappush(heap, (duration, i))
                ptr+=1

            # Pick the smallest time/index. 
            if heap:
                duration, i = heapq.heappop(heap)
                res.append(i)
                time += duration
        
        return res
