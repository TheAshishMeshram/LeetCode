class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        visit = set()

        def dfs(course):
            if course in visit:
                return False

            if graph[course] == []:
                return True

            visit.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visit.remove(course)
            graph[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True