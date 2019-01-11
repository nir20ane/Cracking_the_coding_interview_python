""""** 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
* bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
* Approach:
* for i = 0 to n
* temp= top[i];
* top[i] = left[i]
* left[i] = bottom[i]
* bottom[i] = right[i]
* right[i] = temp
* Time Complexity: O(n^2); Space Complexity O(1)
 */"""
class RotateMatrix(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n / 2):
            if n == 0 or (len(matrix[0]) < n): break  # break if invalid matrix
            first = i  # break first and last
            last = n - i - 1
            for j in range(first, last):
                offset = j - first  # calculate offset
                top = matrix[first][j];
                matrix[first][j] = matrix[last - offset][first]  # left to top
                matrix[last - offset][first] = matrix[last][last - offset] # bottom to left
                matrix[last][last - offset] = matrix[j][last]  # right to bottom
                matrix[j][last] = top  # top to right
        return matrix

rot = RotateMatrix();
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(rot.rotate(matrix))