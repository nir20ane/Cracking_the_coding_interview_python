"""**1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
* Approach:
* Use first row an first column as replacement for the array
* Nullify those rows and columns
* Time Complexity O(n^2)(row*column); Space Complexity O(n)
*/"""

class ZeroMatrix_UsingReplacement(object):
    def zeroMatrix(self, matrix):

        rowhaszero = False
        columnhaszero = False  # use boolean values to 0th row or column has zero

        for j in range(len(matrix[0])):
            if (matrix[0][j] == 0): rowhaszero = True  # update boolean row 0

        for i in range(len(matrix)):
            if(matrix[i][0] == 0): columnhaszero = True  # update boolean column 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):  # iterate from 1 to matrix length, ans use row 0 and column 0 to keep track of zeroes
                if(matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if(matrix[i][0] == 0): self.rowzero(matrix, i)  # if a row has 0, nullify row

        for j in range(1, len(matrix[0])):
            if(matrix[0][j] == 0): self.columnzero(matrix, j)  # if a column has 0, nullify column

        if(rowhaszero): self.rowzero(matrix, 0)  # nullify row 0 if it has 0 value

        if(columnhaszero): self.columnzero(matrix, 0)  # nullify column 0 if it has 0 value

        return matrix

    def rowzero(self, matrix, row):
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    def columnzero(self, matrix, column):
        for i in range(len(matrix)):
            matrix[i][column] = 0

ze = ZeroMatrix_UsingReplacement()
print(ze.zeroMatrix([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))