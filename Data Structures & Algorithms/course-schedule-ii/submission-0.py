class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = [0] * numCourses
        pre = defaultdict(list)

        for cla in prerequisites:
            c, p = cla
            pre[c].append(p)

        visited = set()
        visiting = set()
        

        def dfs(cla):
            if cla in visiting:
                return False
            if cla in visited:
                return True
            
            visiting.add(cla)

            for p in pre[cla]:
                if not dfs(p):
                    return False

            visiting.remove(cla)
            visited.add(cla)
            res.append(cla)

            return True


        for c in range(numCourses):
            if not dfs(c):
                return []

        return res



    
    # each entry is a class and guaranteed to be a pair. 
    # map the class to the prereq

