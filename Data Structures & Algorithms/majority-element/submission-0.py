class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = defaultdict(int)
        most = 0
        res = 0

        for num in nums:
            freq[num] += 1
            if most < freq[num]:
                most += 1
                res = num
        
        return res


