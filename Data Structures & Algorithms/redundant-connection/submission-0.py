class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        def dfs(curr, target, seen):

            if curr == target:
                return True
            
            seen.add(curr)

            for nei in adj[curr]:
                if nei not in seen:
                    if dfs(nei, target, seen):
                        return True
            
            return False
        
        for a, b in edges:

            if dfs(a,b,set()):
                return [a,b]

            adj[a].append(b)
            adj[b].append(a)
            


        
            


        








        return res


            # Check to see how it's connected. 
            # check if it can be the result.
                # criteria: TODO
                # if it fits, great! update the res with the curr edge
                # if it doesnt, continue
                
        # return res

        # We could also use a hashmap to keep track of the node and how many connections it has. 

        # Criteria to be the result 
            # If both nodes are already visited 
            # and are part of the connection