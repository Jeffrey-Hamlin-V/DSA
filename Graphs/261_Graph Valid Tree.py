from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        parent = list(range(n))
        def find(node):
            while node != parent[node]: parent[node] = parent[parent[node]]; node = parent[node]
            return node
        for first, second in edges:
            a,b = find(first),find(second)
            if a == b: return False
            parent[a] = b
        return True
