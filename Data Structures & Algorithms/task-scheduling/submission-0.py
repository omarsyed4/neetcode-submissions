class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        heap = []

        for f in freq.values():
            heapq.heappush(heap, -f)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if q and q[0][1] <= time:
                freq, av = q.popleft()
                heapq.heappush(heap, freq)

            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq < 0:
                    q.append((freq, time + n + 1))

        return time