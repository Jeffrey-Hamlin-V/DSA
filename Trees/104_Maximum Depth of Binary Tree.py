class Solution:
    def maxDepth(self, root) -> int:
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
