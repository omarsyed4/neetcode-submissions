class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for num in nums[1:]:
            tempMax = max(num, num * currMin, num * currMax)
            tempMin = min(num, num * currMin, num * currMax)

            currMax = tempMax
            currMin = tempMin

            res = max(res, currMax)

        return res





'''
[2,4,-3,5,-1]
           ^

maxP = 120

[1,2,8,-24,-120,120]
                ^
'''

# DP approach 

# Keep track of two things. 
    # Product of the current number times all previous numbers 
    # Maximum product up until this point 


# The DP array 
    # Make number of nums elements + 1
    # dp[0] = Gets initialized to 1 for further iterations 

# the max product variable 

# For everything in range 1 to the amount of numbers + 1:
    # Set the element to the current number times `dp[i - 1]`. 
    # Compare that to the current max. 

