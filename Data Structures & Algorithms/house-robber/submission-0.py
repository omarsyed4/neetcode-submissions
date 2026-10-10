class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0 # O(1) space

        for num in nums: # O(n) time
            temp = rob2
            rob2 = max(rob1 + num, rob2)
            rob1 = temp 
        
        return rob2




# At each house, we have to keep track of the house's value. 
# What the maximum was right before 
# What the value could be if the current house is added to the previous maximum. 
