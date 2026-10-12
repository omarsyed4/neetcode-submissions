class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)

            for n in graph[node]:
                if n not in visited: 
                    dfs(n)
        
        dfs(0)

        return len(visited) == n



# Check if the edges are n - 1. 
    # If not, return false. 

# Build the adjacency list. 
# Initialize a 2D array. 
    # Add all the neighbors for that node. 

# Create the visited set. 

# dfs
    # Add it to the visited set. 
    # Iterate through all the neighbors. 
    # Call DFS on the neighbors. 


# return len(visited) == n





"""

Input: n = 5, edges = 

[[0,1],[0,2],[0,3],[1,4]]
                     ^ ^

Output: true

[0] = [1,2,3]
[1] = [0,4]
[2] = [0]
[3] = [0]
[4] = [1]
"""