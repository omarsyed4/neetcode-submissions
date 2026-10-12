class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visiting = set()
        visited = set()

        adj = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            adj[c].append(p)

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for p in adj[course]:
                if not dfs(p):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
            
            