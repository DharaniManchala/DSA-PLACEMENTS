class Solution:
    def maximum_jumps(self,nums,target):
        n=len(nums)
        dp=[-1]*n
        dp[0]=0
        for i in range(n):
            if dp[i]==-1:
                continue
            for j in range(i+1,n):
                if abs(nums[j]-nums[i])<=target:
                    dp[j]=max(dp[j],dp[i]+1)
        return dp[-1]
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,3,6,4,1,2]
    target=2
    print(sol.maximum_jumps(nums,target))  # Output: 3

    #time complexity: O(n^2)
    #space complexity: O(n)
                
                
        
