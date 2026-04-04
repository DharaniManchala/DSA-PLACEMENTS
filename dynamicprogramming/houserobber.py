# House Robber Problem
# Goal: Find maximum money without robbing adjacent houses

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        # edge case
        if n == 1:
            return nums[0]
        
        # dp[i] = max money till index i
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[n-1]


# Example test
if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    sol = Solution()
    print(sol.rob(nums))  # Output: 12