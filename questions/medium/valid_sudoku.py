class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
    print("hello")
    print(row,column,"=",board[row][column])
    for i in range(3*int(row/3),3*int(row/3)+3):
        for j in range(int(column/3),3*int(column/3)+1):
            print(i,j,"=",board[i][j])
    return True
