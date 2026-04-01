class Solution:
    def rotate(self,matrix):
        n=len(matrix)
        rotated=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n-1-i]=matrix[i][j]
        return rotated
    #example
if __name__=="__main__":
    sol=Solution()
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    result=sol.rotate(matrix)
    print(result)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    #time complexity: O(n^2) where n is the number of rows (or columns) in the input matrix
    #space complexity: O(n^2) since we are creating a new matrix to store the rotated values
# optimal solution
class Solution:
    def rotate(self,matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix
    #example
if __name__=="__main__":
    sol=Solution()
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    result=sol.rotate(matrix)
    print(result)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    #time complexity: O(n^2) where n is the number of rows (or columns) in the input matrix
    #space complexity: O(1) since we are rotating the matrix in place without using any additional data structures
