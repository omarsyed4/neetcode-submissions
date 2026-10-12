class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        islands = 0

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)        
            graph[b].append(a)        
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in graph[node]:
                dfs(n)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                islands += 1
        
        return islands

        


# visited set

# islands = 0

# for edge
    # not in visited?
    #   islands += 1

    