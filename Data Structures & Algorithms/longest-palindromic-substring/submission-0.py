class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ''

        for i, c in enumerate(s):

            odd = self.helper(s,i,i)
            even = self.helper(s,i,i+1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
            
        return res



    def helper(self, s: str, front:int, back:int) -> str:

        # Keep going until both are not equal
        while front >= 0 and back < len(s) and s[front] == s[back]:
            front -= 1
            back += 1
        
        return s[front + 1:back]
        





# Keep a tally of what the longest length was so far. 
# Every palindrome needs at least two letters. 
# For each letter, and get the value and its index. 
    # We should check each letter and if the letters next to it are equal. 
    # If they are equal, then continue exploring this as an option. 
    # If one of them is the same letter, then we can save that as the longest substring and move forward. 
    # If none of them are equal, move on to the next letter. 

# Helper function to determine a palindrome from the center 
# Start the pointer at the center. 
# Continue to increment one and decrement one, and make sure that both pointers are always equal.
# When they are unequal, return those indices. 
# Save that as the longest substring. 