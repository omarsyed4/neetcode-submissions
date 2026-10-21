class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        hm = defaultdict(list)
        heap = []
        res = []
        
        for p in points:
            # formula
            ans = p[0]**2 + p[1]**2
            heapq.heappush(heap, ans)
            hm[ans].append(p)
        
        while len(res) < k:
            res.append(hm[heapq.heappop(heap)].pop())
        
        return res
        
