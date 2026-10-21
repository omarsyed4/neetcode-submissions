class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # make a max heap
        heap = []

        # add 
        for n in nums:
            heapq.heappush(heap, -n)

        # pop
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)