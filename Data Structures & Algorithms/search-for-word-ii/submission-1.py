class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        ptr = self

        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        rows = len(board)
        cols = len(board[0])

        visit = set()
        res = set()

        def dfs(word, node, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if (r,c) in visit:
                return
            
            if board[r][c] not in node.children:
                return
            
            visit.add((r,c))

            node = node.children[board[r][c]]

            word += board[r][c]

            if node.end:
                res.add(word)
            
            visit.add((r,c))

            dfs(word, node, r-1, c)
            dfs(word, node, r+1, c)
            dfs(word, node, r, c-1)
            dfs(word, node, r, c+1)

            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs("", root, r, c)

        return list(res)


# Keep a result array to append words. 


# For each word 
    # Call DFS with the board, the word, and the two coordinates (the rows and columns). 
    # Initialize a visited set. 
    # DFS ( word, r,c, board ) -> bool
        # If not word, return true. 
            # Also, make sure that the visited set is clear. 
        # Make sure we're within bounds. 
        # Check if the coordinates are in the visited set. 

        # Get the first letter. 

        # If the letter matches the current letter, explore all other directions. 
        # If it doesn't return false 
            # Make sure the visited set is clear. 

# Return result. 
