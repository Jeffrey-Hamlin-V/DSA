class Solution:
    def cloneGraph(self, node):
        if not node: return None
        copies = {}
        def clone(current):
            if current in copies: return copies[current]
            copy = Node(current.val); copies[current] = copy
            copy.neighbors = [clone(neighbor) for neighbor in current.neighbors]
            return copy
        return clone(node)
