class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        longest = 0
        dp = [1] * len(nums)

        for i, upper in enumerate(nums):
            for j in range(i):
                curr = nums[j]

                if curr < upper:
                    dp[i] = max(dp[i], dp[j] + 1)
                
            longest = max(longest, dp[i])
        
        return longest
        



# upper
# curr


# Set a variable to track the longest. 

# number 2
# Lower bound = 1
# For upper in numbers 
    # For lower number in beginning to current index 
        # If lower number is greater than current number, then skip. 
        # Initialize the lower bound. 
        # Check if the lower number is valid. 
            # Add it to the visited set. 
            # Increase current by 1.

    # Get the maximum between the current and the longest. 

# Return longest. 