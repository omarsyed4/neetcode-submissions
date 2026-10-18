class Solution:
    def validPalindrome(self, s: str) -> bool:


        def isPal(L, R):
            while L < R:
                if s[L] == s[R]:
                    L += 1
                    R -= 1
                else:
                    return False
        
            return True
        
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                if isPal(L, R-1) or isPal(L+1, R):
                    return True
                else:
                    return False
        return True