"""**1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
* Approach:
* Have two boolean arrays to keep track of row and column that has zero
* Nullify those rows and columns
* Time Complexity O(n^2)(row*column); Space Complexity O(n)
*/"""
class ZeroMatrix_WithLists(object):
    def zeroMatrix(self, matrix):
        row_lst = [False]*len(matrix)  # have two lists with boolean values
        column_lst = [True]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: # track the row and column that has zero
                    row_lst[i] = True
                    column_lst[j] = True

        for i in range(len(row_lst)):
            if(row_lst[i]): self.rowzero(matrix, row_lst[i])  # if zero in row, nullify row

        for j in range(len(column_lst)):
            if(column_lst[j]): self.columnzero(matrix, column_lst[j])  # if zero in column, nullify column

        return matrix

    def rowzero(self, matrix, row):
        for j in range(len(matrix[0])):
            matrix[row][j] = 0  # make row as zero

    def columnzero(self, matrix, column):
        for i in range(len(matrix)):
            matrix[i][column] = 0  # make column as zero

ze = ZeroMatrix_WithLists()
print(ze.zeroMatrix([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))