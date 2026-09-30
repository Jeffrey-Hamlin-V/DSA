class Solution:
    def isValidBST(self, root) -> bool:
        def valid(node, low, high):
            if not node: return True
            return low < node.val < high and valid(node.left, low, node.val) and valid(node.right, node.val, high)
        return valid(root, float('-inf'), float('inf'))
