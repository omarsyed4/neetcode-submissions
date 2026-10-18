class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest = float("inf")
        prefix = ""

        # finds prefix
        for s in strs:
            shortest = min(shortest, len(s))
            if shortest == len(s):
                prefix = s
        
        # Compares prefix to other words 
        for s in strs:
            ptr = 0
            while ptr < len(prefix):
                if s[ptr] == prefix[ptr]:
                    ptr += 1
                else:
                    prefix = prefix[:ptr]
                    break

        return prefix
        