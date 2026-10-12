from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        def find(node):
            if parent[node] != node: parent[node] = find(parent[node])
            return parent[node]
        for a,b in edges:
            a,b = find(a),find(b)
            if a != b: parent[a] = b
        return len({find(node) for node in range(n)})
