# using prefixsum concept
class Solution:
    def pivotindex(self,nums):
        n=len(nums)
        sum=0
        for i in range(n):
            sum+=nums[i]
        leftsum=0
        for i in range(n):
            rightsum=sum-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,7,3,6,5,6]
    result=sol.pivotindex(nums)
    print(result)  # Output: 3

    #time complexity: O(n) where n is the length of the input array
    #space complexity: O(1) since we are using only a constant amount of extra space
        
        