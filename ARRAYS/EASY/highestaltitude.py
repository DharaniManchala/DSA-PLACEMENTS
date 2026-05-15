# this problem is solved using prefixsum
class Solution:
    def highestaltitude(self,nums):
        sum=0
        maxaltitude=0
        for i in range(len(nums)):
            sum+=nums[i]
            maxaltitude=max(maxaltitude,sum)
        return maxaltitude
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[-5,1,5,0,-7]
    result=sol.highestaltitude(nums)
    print(result)  # Output: 1

    #time complexity: O(n) where n is the length of the input array
    #space complexity: O(1) since we are using only a constant amount of extra space
