class Solution:

    def sqrt(self, x):

        if x < 2:
            return x

        left = 1
        right = x

        answer = 0

        while left <= right:

            mid = (left + right) // 2

            square = mid * mid

            if square == x:
                return mid

            elif square < x:
                answer = mid
                left = mid + 1

            else:
                right = mid - 1

        return answer


# Example
if __name__ == "__main__":

    sol = Solution()

    x = 8

    print(sol.sqrt(x))