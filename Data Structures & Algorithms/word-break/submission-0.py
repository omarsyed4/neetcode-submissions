class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * len(s)

        confirmed = set()

        for i in range(len(s)):

            # The entire word in the dictionary?
            if (s[0:i+1]) in wordDict:
                dp[i] = True
            else:
                # Words from the last confirmed state 
                for j in confirmed:
                    if (s[j+1:i+1]) in wordDict:
                        dp[i] = True
                
            if dp[i]: confirmed.add(i)
        
        return dp[len(s) - 1]
                    

            

        
        

# We can traverse the array and keep track of whether this array is something we can actually decode. The answer will continue to build on itself. 

# It's very clearly a dynamic programming problem. 

# Start by creating an array of false variables for the length of `s`. 
# Create a set for confirmed word indexes. 
# Iterate through the string. 
# For each index:
    # Look to see if that entire word is in the dictionary. 
    # For each saved index in the confirmed set 
        # Look to see if a word from the last portion of "true" is in the dictionary. 
    # Save the indexes where the word is confirmed in the dictionary. 



""""catsincars"
    ^

wordDict = ["cats","cat","sin","in","car"]
confirmed = (2)

[F,F,T,T,F,F,F,F,F,F]
^"""