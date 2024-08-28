board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


class Solution:
    "https://leetcode.com/problems/valid-sudoku/description/"
    def isValidSudoku(self, board):
        def validate_board_size(board):
            if len(board) != 9 :
                return False
            else:
                return True
            
        def validate_lines_size(board):
            for i in board:
                if len(i) != 9:
                    return False
                else:
                    return True
                
        def validate_line(line):
            nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in line:
                if i != ".":
                    nums[int(i)]+=1
            for i in nums:
                if i > 1:
                    return False
            return True        
        
        def validate_lines_horizontal(board):
            for i in board:
                if validate_line(i):
                    pass
                else:
                    return False
            return True
        
        def validate_lines_vertical(board):
            for i in range(len(board)):
                line = [row[i] for row in board]
                if validate_line(line):
                    pass
                else:
                    return False
            return True

        def validate_squares(board):
            def split_to_squares(board):
                squares = []

                squares.append(
                    [
                        [board[0][0], board[0][1], board[0][2]],
                        [board[1][0], board[1][1], board[1][2]],
                        [board[2][0], board[2][1], board[2][2]]
                    ])
                squares.append(
                    [
                        [board[0][3], board[0][4], board[0][5]],
                        [board[1][3], board[1][4], board[1][5]],
                        [board[2][3], board[2][4], board[2][5]]
                    ])
                squares.append(
                    [
                        [board[0][6], board[0][7], board[0][8]],
                        [board[1][6], board[1][7], board[1][8]],
                        [board[2][6], board[2][7], board[2][8]]
                    ])
                
                squares.append(
                    [
                        [board[3][0], board[3][1], board[3][2]],
                        [board[4][0], board[4][1], board[4][2]],
                        [board[5][0], board[5][1], board[5][2]]
                    ])
                squares.append(
                    [
                        [board[3][3], board[3][4], board[3][5]],
                        [board[4][3], board[4][4], board[4][5]],
                        [board[5][3], board[5][4], board[5][5]]
                    ])
                squares.append(
                    [
                        [board[3][6], board[3][7], board[3][8]],
                        [board[4][6], board[4][7], board[4][8]],
                        [board[5][6], board[5][7], board[5][8]]
                    ])
                
                squares.append(
                    [
                        [board[6][0], board[6][1], board[6][2]],
                        [board[7][0], board[7][1], board[7][2]],
                        [board[8][0], board[8][1], board[8][2]]
                    ])
                squares.append(
                    [
                        [board[6][3], board[6][4], board[6][5]],
                        [board[7][3], board[7][4], board[7][5]],
                        [board[8][3], board[8][4], board[8][5]]
                    ])
                squares.append(
                    [
                        [board[6][6], board[6][7], board[6][8]],
                        [board[7][6], board[7][7], board[7][8]],
                        [board[8][6], board[8][7], board[8][8]]
                    ])

                return squares
            
            def validate_square(square):
                nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                counter = 0
                for i in square:
                    for j in i:
                        if j != ".":
                            nums[int(j)] += 1
                        counter+=1
                for i in nums:
                    if i > 1:
                        return False
                return True
            for i in split_to_squares(board):
                if validate_square(i):
                    pass
                else:
                    return False
            return True
        
        if validate_board_size(board) and validate_lines_size(board) and validate_lines_horizontal(board) and validate_lines_vertical(board) and validate_squares(board):
            return True
        else:
            return False
            

s = Solution()
print(s.isValidSudoku(board))