from collections import deque

class Codec:
    def serialize(self, root):
        if not root: return ''
        values, queue = [], deque([root])
        while queue:
            node = queue.popleft()
            if node: values.append(str(node.val)); queue.extend([node.left, node.right])
            else: values.append('N')
        return ','.join(values)

    def deserialize(self, data):
        if not data: return None
        values = data.split(','); root = TreeNode(int(values[0])); queue = deque([root]); index = 1
        while queue:
            node = queue.popleft()
            if values[index] != 'N': node.left = TreeNode(int(values[index])); queue.append(node.left)
            index += 1
            if values[index] != 'N': node.right = TreeNode(int(values[index])); queue.append(node.right)
            index += 1
        return root
