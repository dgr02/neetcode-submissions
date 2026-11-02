class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for x in board:

            row = {}

            for y in x:
                
                if y == ".":
                    continue

                if y in row:
                    return False

                else:
                    row[y] = "present"
        
        for x in list(zip(*board)):

            col = {}

            for y in x:
                
                if y == ".":
                    continue

                if y in col:
                    return False

                else:
                    col[y] = "present"

        for x in range(9):

            square = {}
        
            row_start = (x // 3) * 3
            col_start = (x % 3) * 3

            for i in range(3):

                for j in range(3):

                    y = board[row_start + i][col_start + j]

                    if y == ".":
                        continue

                    if y in square:
                        return False

                    else:
                        square[y] = "present"
        
        return True




