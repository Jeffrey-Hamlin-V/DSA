class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot: return True
        if not root: return False
        return self.same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, first, second):
        if not first and not second: return True
        if not first or not second or first.val != second.val: return False
        return self.same(first.left, second.left) and self.same(first.right, second.right)
