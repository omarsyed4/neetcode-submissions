"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        clones = {}

        def dfs(curr):

            if curr in clones:
                return clones[curr]
            
            copy = Node(curr.val)

            clones[curr] = copy

            for n in curr.neighbors:
                c_n = dfs(n)
                copy.neighbors.append(c_n)
            
            return copy
        
        return dfs(node)


        