from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root: return []
        result, queue = [], deque([root])
        while queue:
            result.append([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return result
