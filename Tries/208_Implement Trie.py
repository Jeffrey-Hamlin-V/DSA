class TrieNode:
    def __init__(self): self.children, self.end = {}, False

class Trie:
    def __init__(self): self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word: node = node.children.setdefault(char, TrieNode())
        node.end = True
    def search(self, word):
        node = self._node(word); return bool(node and node.end)
    def startsWith(self, prefix): return self._node(prefix) is not None
    def _node(self, text):
        node = self.root
        for char in text:
            if char not in node.children: return None
            node = node.children[char]
        return node
