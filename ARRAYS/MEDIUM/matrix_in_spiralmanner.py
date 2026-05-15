class Solution:
    def spiralOrder(self, matrix):

        # answer array
        ans = []

        # boundaries
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # loop until boundaries cross
        while top <= bottom and left <= right:

            # 1. LEFT → RIGHT
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            top += 1

            # 2. TOP → BOTTOM
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])

            right -= 1

            # 3. RIGHT → LEFT
            # check because row may not exist
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])

                bottom -= 1

            # 4. BOTTOM → TOP
            # check because column may not exist
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])

                left += 1

        return ans


# Example Usage
if __name__ == "__main__":

    sol = Solution()

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
    ]

    print(sol.spiralOrder(matrix))
    # time complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix
    # space complexity: O(m*n) for the answer array that stores all the elements in