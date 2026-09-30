class Solution:
    def buildTree(self, preorder, inorder):
        positions = {value: index for index, value in enumerate(inorder)}
        def build(left, right):
            if left > right: return None
            value = preorder.pop(0)
            root = TreeNode(value)
            middle = positions[value]
            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)
            return root
        return build(0, len(inorder) - 1)
