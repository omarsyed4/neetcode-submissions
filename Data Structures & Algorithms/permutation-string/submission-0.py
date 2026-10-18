class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = len(s1)

        if window > len(s2):
            return False

        freq1 = Counter(s1)
        freq2 = Counter(s2[:window])

        if freq1 == freq2:
            return True

        L = 0
        R = window - 1
        while R < len(s2) - 1:

            freq2[s2[L]] -= 1

            if freq2[s2[L]] == 0:
                del freq2[s2[L]]

            L += 1
            R += 1

            freq2[s2[R]] += 1

            if freq2 == freq1:
                return True
        
        return False





# window = len(s1)

# store the freq of each letter

# for l in word

# is R - L < window
    # check to see if its in s1
        # check if any of those letters  left
            # subtract from freq

'''

window 2

freq = 
a : 1
b : 1

"lecabee"
    ^

'''