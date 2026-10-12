class WordDictionary:
    def __init__(self): self.children, self.end = {}, False
    def addWord(self, word):
        node = self
        for char in word: node = node.children.setdefault(char, WordDictionary())
        node.end = True
    def search(self, word):
        def find(node, index):
            if index == len(word): return node.end
            char = word[index]
            return any(find(child, index + 1) for child in node.children.values()) if char == '.' else char in node.children and find(node.children[char], index + 1)
        return find(self, 0)
