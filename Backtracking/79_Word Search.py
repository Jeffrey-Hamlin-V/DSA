from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])

        def search(row: int, column: int, index: int) -> bool:
            if index == len(word):
                return True
            if row < 0 or row == rows or column < 0 or column == columns or board[row][column] != word[index]:
                return False

            character = board[row][column]
            board[row][column] = "#"
            found = (
                search(row + 1, column, index + 1)
                or search(row - 1, column, index + 1)
                or search(row, column + 1, index + 1)
                or search(row, column - 1, index + 1)
            )
            board[row][column] = character
            return found

        return any(search(row, column, 0) for row in range(rows) for column in range(columns))
