class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = sorted(set(nums))
        
        un = len(seen)

        nums[:un] = seen

        return un
        