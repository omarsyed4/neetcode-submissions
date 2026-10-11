class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (1 + amount )
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                # The amount that we're looking at is I. 
                # Get the remainder and find that in our DP array. 
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        
        if dp[amount] == (amount + 1):
            return -1

        
        return dp[amount]







# Create a DP array of the amount of coins we have. 
# For each index, we can keep track of what was the minimum amount of coins up to this point? 
# We can just return the end of the DP array. 