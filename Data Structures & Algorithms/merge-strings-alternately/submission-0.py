class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []

        ptr1 = 0
        ptr2 = 0

        wordOneLen = len(word1)
        wordTwoLen = len(word2)

        while (ptr1 < wordOneLen) and (ptr2 < wordTwoLen):
            res.append(word1[ptr1])
            res.append(word2[ptr2])
            ptr1+=1
            ptr2+=1

        if ptr1 >= wordOneLen:
            res.append(word2[ptr2:])
        elif ptr2 >= wordTwoLen:
            res.append(word1[ptr1:])
        
        
        return ''.join(res)


            

        
        