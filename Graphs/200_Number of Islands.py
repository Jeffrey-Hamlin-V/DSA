from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, count = len(grid), len(grid[0]), 0
        def visit(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1': return
            grid[r][c] = '0'
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)): visit(r+dr,c+dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1': count += 1; visit(r,c)
        return count
