class Solution:
    def frogjump(self,heights):
        n=len(heights)
        dp=[0]*n
        for i in range(1,n):
            jump1=dp[i-1]+abs(heights[i]-heights[i-1])
            jump2=float('inf')
            if i>1:
                jump2=dp[i-2]+abs(heights[i]-heights[i-2])
            dp[i]=min(jump1,jump2)
        return dp[-1]
# example usage
if __name__=="__main__":
    sol=Solution()
    heights=[10,30,40,20]
    result=sol.frogjump(heights)
    print(result)  # Output: 30

    #time complexity: O(n) where n is the number of elements in the heights array
    #space complexity: O(n) for storing the dp array which contains the minimum energy required to reach each stone



