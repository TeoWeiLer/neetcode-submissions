class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        # square goes 0 to 8 (the 9 boxes)
        for square in range(9):
            seen = set()
            # i and j move us INSIDE the 3x3 box we pick
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    # // is SLOW: It stays 0 for three boxes, then 3, then 6.
                    # It tells us which "FLOOR" (top, middle, bottom) we are on.
                    col = (square % 3) * 3 + j
                    # % is FAST: It resets 0, 3, 6, 0, 3, 6 every time.
                    # It tells us which "ROOM" (left, center, right) we are in.

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True