#Question can be found here:
#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            if target<=matrix[i][columns-1]:
                for j in range(columns):
                    if target==matrix[i][j]:
                        return True
        return False
