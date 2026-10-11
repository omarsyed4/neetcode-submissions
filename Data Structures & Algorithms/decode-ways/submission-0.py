class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [0] * (n + 1)

        # First element is 1. 
        dp[0] = 1

        for i in range(1, n+1):

            # Single-digit decode 
            # Can it be decoded individually? 
            if s[i-1] != '0':
                dp[i] += dp[i - 1]

            # Double-digit decode 
            # Can it be decoded with the previous two numbers? 
            if i >= 2:
                if 10 <= int(s[i-2:i]) <= 26:
                    dp[i] += dp[i - 2]
        
        return dp[n]







# Leading zeros are not possible. 
# We pay attention to digits individually, but keep in mind: if it's an individual digit that is non-zero, by default it maps to a letter. 
# We also have to be mindful of when a zero is added to the end of a number. 
# And we have to skip zeros as they come. 
# Track when it's valid to skip a zero. 



# For each number
# Skip if it's a zero, and the last number took the zero. 
# we have to evaluate its individual letter. 
# Then we have to evaluate if it's joined with the next number. Does it fall under 26? 


