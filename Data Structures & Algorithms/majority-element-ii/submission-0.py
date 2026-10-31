class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        thold = n // 3

        uniq = set(nums)

        res = []

        freq = Counter(nums)

        for u in uniq:
            if freq[u] > thold:
                res.append(u)
            
        return res
