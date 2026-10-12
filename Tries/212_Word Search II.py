from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for char in word: node = node.setdefault(char, {})
            node['$'] = word
        result, rows, cols = [], len(board), len(board[0])
        def dfs(row, col, node):
            char = board[row][col]
            if char not in node: return
            node = node[char]
            word = node.pop('$', None)
            if word: result.append(word)
            board[row][col] = '#'
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#': dfs(nr, nc, node)
            board[row][col] = char
        for row in range(rows):
            for col in range(cols): dfs(row, col, root)
        return result
