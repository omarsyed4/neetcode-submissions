class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i + 1)

            res += odd + even
        return res

    def helper(self, s: str, front: int, back: int) -> int:

        poss = 0

        while front >= 0 and back < len(s) and s[front] == s[back]:

            front -= 1
            back += 1
            poss += 1
        
        return poss







# Since each character can be a substring, initialize the result to the length of the string first. 

# Helper function to get the palindromic substring if the current char is the center of the substring 