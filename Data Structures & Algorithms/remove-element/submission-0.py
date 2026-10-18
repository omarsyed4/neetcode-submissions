class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        res = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[res] = num
                res += 1
        return res
# For every single number 
    # If it's not equal to the value update the ctr

# return counter
        