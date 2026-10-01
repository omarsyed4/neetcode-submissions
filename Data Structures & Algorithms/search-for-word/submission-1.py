class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        columns = len(board[0])
        visited = set()

        def dfs(r, c, letter):

            if letter == len(word):
                return True

            if r >= rows or r < 0 or c >= columns or c < 0:
                return False
            
            if (r, c) in visited:
                return False

            if board[r][c] != word[letter]:
                return False
            
            visited.add((r,c))

            letter += 1

            found = (
                dfs(r - 1, c, letter) 
                or dfs(r + 1, c, letter)
                or dfs(r, c - 1, letter)
                or dfs(r, c + 1, letter)
            )
            visited.remove((r,c))
            return found

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0): 
                    return True
        
        return False






'''

The reasons we would reject a cell are:
- If it's not the letter we want
- If it's out of bounds
- If it's a cell that we've visited

After we found the correct letter 
Increment the letter by one. 
Recursively call the function on the next letter in all four directions. 



'''
