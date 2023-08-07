from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #This solution uses sets to create a unique list of numbers, and if it finds a match, returns false
        # rows = defaultdict(set)
        # cols = defaultdict(set)
        # squares = defaultdict(set)
        # for i in range(9):
        #     for j in range(9):
        #         if (board[i][j] == "."):
        #             continue
        #         elif (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i // 3, j //3)]):
        #             return False
        #         else:
        #             rows[i].add(board[i][j])
        #             cols[j].add(board[i][j])
        #             squares[(i // 3, j // 3)].add(board[i][j])
        # return True


        #This is my solution, it doesn't have good runtime or memory usage, but made the most sense to me logically
        #MY SOLUTION
        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric() and (not isValidColumn(board,i,j) or not isValidRow(board,i,j) or not isValidBox(board,i,j)):
                    return False
        return True
    

def isValidRow(board,row,column) -> bool:
    for i in range(9):
        if i!=column and board[row][column]==board[row][i]:
            print("__",board[row][column],board[row][i])
            return False
    return True

def isValidColumn(board,row,column) -> bool:
    for i in range(9):
        if i!=row and board[row][column]==board[i][column]:
            return False
    return True

def isValidBox(board,row,column) -> bool:
    for i in range(3*int(row/3),3*int(row/3)+3):
        for j in range(3*int(column/3),3*int(column/3)+3):
            if (row!=i and column!=j and board[row][column]==board[i][j]):
                return False
    return True
