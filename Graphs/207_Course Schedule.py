from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites: graph[course].append(prerequisite)
        visiting, done = set(), set()
        def dfs(course):
            if course in visiting: return False
            if course in done: return True
            visiting.add(course)
            if not all(dfs(prerequisite) for prerequisite in graph[course]): return False
            visiting.remove(course); done.add(course); return True
        return all(dfs(course) for course in range(numCourses))
