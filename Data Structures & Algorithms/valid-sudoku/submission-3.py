class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 # one integer per row
        cols = [0] * 9 # one integer per col
        squares = [0] * 9 # one integer per 3x3 square

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c]) - 1 
                # Subtract 1 so digits 1–9 map to bit positions 0–8. 
                # This just makes the shifting cleaner (no wasted bit 0).
                if (1 << val) & rows[r]: 
                    # Build the bitmask for this digit
                    # creates a number with only the bit at position val set:
                    # & is bitwise AND. It checks whether the bit for this digit is already set in the row's integer.
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                # |= is bitwise OR-assign. It sets the bit for this digit without touching any others.
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)
                #Maps any (r, c) to one of the 9 squares — r // 3 gives the box row (0–2), c // 3 gives the box column (0–2).

        return True
        # faster and more memory-efficient, at the cost of readability.